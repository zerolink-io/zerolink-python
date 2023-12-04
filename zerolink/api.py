import os
from typing import Any, Generator, List, Optional, Union

import zerolink.attribute as attr
import zerolink.req as req
from zero_link_client.models import (
    AttributeType,
    CreateAttribute,
    CreateEntity,
    CreateRule,
    CreateRuleContext,
    CreateTriple,
    ExtractModel,
    SpatialAssumption,
    TemporalAssumption,
    TextExtract,
    WorldAssumption,
    EntityType,
    ResultStatus,
)
from zero_link_client.types import File
from zerolink.extract import read_docx
from zerolink.settings import api_key

# ------------------------------------------------------------------------
# Entities
# ------------------------------------------------------------------------


class Entity(object):
    """
    An entity is an object/node in a knowledge graph.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str] = None,
        kg: Optional["KnowledgeGraph"] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.kg = kg

    def instance(self, class_: "Entity") -> "Fact":
        """
        Add a fact that this entity is an instance of a class.
        """
        if self.kg:
            return self.kg.add_fact(self, "instance of", class_)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def is_a(self, class_: "Entity") -> "Fact":
        """
        Add a fact that this entity is an instance of a class.
        """
        return self.instance(class_)

    def subclass(self, superclass: "Entity") -> "Fact":
        """
        Add a fact that this entity is a subclass of a superclass.
        """
        if self.kg:
            return self.kg.add_fact(self, "subclass of", superclass)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def is_type(self, type_: "Entity") -> "Fact":
        """
        Add a fact that this entity is a subclass of a superclass.
        """
        if self.kg:
            return self.kg.add_fact(self, "is subclass", type_)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def quality(self, quality: "Entity") -> "Fact":
        """
        Add a fact that this entity has a quality.
        """
        if self.kg:
            return self.kg.add_fact(self, "has quality", quality)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def characteristic(self, characteristic: "Entity") -> "Fact":
        """
        Add a fact that this entity has a characteristic.
        """
        if self.kg:
            return self.kg.add_fact(self, "has characteristic", characteristic)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def part_of(self, whole: "Entity") -> "Fact":
        """
        Add a fact that this entity is part of another entity.
        """
        if self.kg:
            return self.kg.add_fact(self, "part of", whole)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def add_fact(self, predicate: str, object: "Entity") -> "Fact":
        """
        Add an arbitrary fact about this entity.
        """
        if self.kg:
            return self.kg.add_fact(self, predicate, object)
        else:
            raise ValueError("Not attached to a knowledge graph")

    def add_attribute(self, attribute: str, value: Any) -> None:
        """
        Add an attribute to this entity.
        """
        if self.kg:
            self.kg.add_attribute(self, attribute, value)
        else:
            raise ValueError("Not attached to a knowledge graph")

    @property
    def user_entity(self) -> bool:
        # If the id starts with EU then it is a user entity, otherwise it is a
        # foundation entity
        return self.id.startswith("EU")

    def ontology(self):
        return ontology(self.id)

    def __str__(self) -> str:
        return f"{self.name} : ({self.id})"

    def __repr__(self) -> str:
        return f'<Entity id="{self.id}" name="{self.name}" description="{self.description}">'


class Relation(object):
    """
    A relation is an edge in a knowledge graph.
    """

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} : ({self.id})"

    def __repr__(self):
        return f'<Relation id="{self.id}" name="{self.name}">'


class Fact(object):
    def __init__(self, id: str, subject: str, predicate: str, object: str, kg=None):
        self.id = id
        self.subject = subject
        self.predicate = predicate
        self.object = object
        self.kg = kg

    def __str__(self) -> str:
        return f"{self.subject} {self.predicate} {self.object}"

    def __rep__(self) -> str:
        return (
            f'<Fact "{self.subject}" "{self.predicate}" "{self.object}" id="{self.id}">'
        )


# ------------------------------------------------------------------------
# Knowledge Graph
# ------------------------------------------------------------------------


class KnowledgeGraph(object):
    name: str
    session_id: int

    def __repr__(self):
        return f'<KnowledgeGraph name="{self.name}" session_id="{self.session_id}">'

    def ask(
        self,
        question: str,
        spatial_assumption: SpatialAssumption = SpatialAssumption.EARTH,
        temporal_assumption: TemporalAssumption = TemporalAssumption.CURRENT,
        world: WorldAssumption = WorldAssumption.PARTIAL,
        reasoners: Optional[list[str]] = None,
        **kwargs,
    ) -> "Result":
        rep = req.ask_question(self.session_id, question, **kwargs)

        if rep is None:
            return Result(data=[], status=ResultStatus.EMPTY)

        if rep.msg == "Found the answer":
            return Result(data=rep.answers, status=ResultStatus.ANSWERS)
        else:
            return Result(data=[], status=ResultStatus.EMPTY)

    def add_entity(
        self, name: str, type: Optional[Union[EntityType, Entity, str]] = None
    ) -> Entity:
        raise ValueError("Cannot add entity to a read-only knowledge graph")

    def add_fact(self, s: Entity, p: str, o: Entity) -> Fact:
        raise ValueError("Cannot add fact to a read-only knowledge graph")

    def add_rule(self, rule: str, ctx: Optional[dict[str, Any]] = None) -> str:
        raise ValueError("Cannot add rule to a read-only knowledge graph")

    def add_attribute(self, e: Entity, a: str, v: Any) -> Fact:
        raise ValueError("Cannot add attribute to a read-only knowledge graph")

    @property
    def entities(self) -> List[Entity]:
        raise NotImplementedError()

    @property
    def facts(self) -> List[Fact]:
        raise NotImplementedError()


class Foundation(KnowledgeGraph):
    """
    The Foundation knowledge graph is a collection of entities and relations
    that are common to all knowledge graphs and form the foundation of
    commonsense reasoning. The graph is read-only.
    """

    def __init__(self) -> None:
        self.name = "Foundation"

    def entity(self, name: str) -> Entity:
        """
        Get a foundation entity by name.
        """
        ents = list(find_entity(name))
        if len(ents) == 0:
            raise ValueError(f"Entity '{name}' not found")
        else:
            return ents[0]

    def property(self, name: str) -> Relation:
        """
        Get a foundation property by name.
        """
        rels = list(find_relation(name))
        if len(rels) == 0:
            raise ValueError(f"Relation '{name}' not found")
        else:
            return rels[0]

    def attribute(self, name: str) -> Relation:
        """
        Get a foundation attribute by name.
        """
        rels = list(find_relation(name))
        if len(rels) == 0:
            raise ValueError(f"Relation '{name}' not found")
        else:
            return rels[0]

    def reasoner(self, name: str):
        """
        Get a foundation reasoner by name.
        """
        reasoners = set(req.get_reasoners(name))
        if name in reasoners:
            return name
        else:
            raise ValueError(f"Reasoner '{name}' not found")


class UserKnowledgeGraph(KnowledgeGraph):
    """
    A knowledge graph is a collection of entities and relations.
    """

    def __init__(self, session_id: int, name: str):
        self.name = name
        self.session_id = session_id

    @property
    def entities(self) -> List[Entity]:
        rep = req.get_session_entities_list(self.session_id)
        return [
            Entity(id=e.id, name=e.entity, description=e.desc, kg=self) for e in rep
        ]

    @property
    def facts(self) -> List[Fact]:
        rep = req.get_session_facts_list(self.session_id)
        return [
            Fact(id=f.id, subject=f.subject, predicate=f.predicate, object=f.object_)
            for f in rep
        ]

    def add_entity(
        self, name: str, type: Optional[Union[EntityType, Entity, str]] = None
    ) -> Entity:
        if isinstance(type, EntityType):
            body = CreateEntity(name, entity_type=type)
        elif isinstance(type, Entity):
            body = CreateEntity(name, entity_str=type.id)
        elif isinstance(type, str):
            body = CreateEntity(name, entity_str=type)
        elif type is None:
            body = CreateEntity(name)
        else:
            raise ValueError("Invalid type")

        rep = req.add_entity(self.session_id, body)
        return Entity(id=rep.id, name=rep.entity, description=None, kg=self)

    def get_or_add_entity(
        self, name: str, type: Union[EntityType, Entity, str]
    ) -> Entity:
        raise NotImplementedError()

    def add_relation(self, *args, **kwargs):
        """
        Add a relation to a user knowledge graph.
        """
        raise NotImplementedError()

    def add_attribute(self, e: Entity, a: str, v: Any):
        """
        Add an attribute to a user knowledge graph.
        """
        value = attr.value(v)
        body = CreateAttribute(
            subject=e.id,
            predicate=a,
            attribute=value,
        )
        rep = req.add_attribute(self.session_id, body)
        if rep.success:
            pass
        else:
            raise ValueError("Failed to add attribute")

    def add_fact(self, s: Entity, p: str, o: Entity) -> Fact:
        """
        Add a fact to a user knowledge graph.
        """
        assert isinstance(s, Entity)
        assert isinstance(o, Entity)
        assert isinstance(p, str)

        if o.id == s.id:
            raise ValueError("Subject and object cannot be the same")

        body = CreateTriple(
            user_subject=s.id,
            predicate=p,
            user_object=o.id,
        )
        rep = req.add_triple(self.session_id, body)
        return Fact(
            id=rep.id, subject=rep.subject, predicate=rep.predicate, object=rep.object_
        )

    def add_rule(self, rule: str, ctx: Optional[dict[str, Any]] = None) -> str:
        """
        Add a rule to a user knowledge graph.
        """
        if ctx and len(ctx) > 255:
            raise ValueError("Context is too large")

        if ctx:
            ctx_mapping = {k: v.id for k, v in ctx.items()}
        else:
            ctx_mapping = {}
        context = CreateRuleContext.from_dict(ctx_mapping)
        body = CreateRule(rule, context=context)
        rep = req.post_rule(self.session_id, body)
        return rep.id

    @staticmethod
    def create(name: str) -> KnowledgeGraph:
        """
        Create a new knowledge graph.
        """
        rep = req.post_session(api_key, name=name)
        if rep is None:
            raise ValueError("Failed to create knowledge graph")
        return UserKnowledgeGraph(rep.id, rep.name)


# ------------------------------------------------------------------------
# Relations
# ------------------------------------------------------------------------


class Attribute(Relation):
    """
    An attribute is a relation between an entity and a value.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        domain: EntityType,
        attribute_type: AttributeType,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.domain = domain

    def __repr__(self) -> str:
        return (
            f"<Attribute id={self.id} name={self.name} description={self.description}>"
        )


class Property(Relation):
    """
    A property is a relation between two entities.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        domain: EntityType,
        codomain: EntityType,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.domain = domain
        self.codomain = codomain

    def __repr__(self) -> str:
        return (
            f"<Property id={self.id} name={self.name} description={self.description}>"
        )


class Result(object):
    """
    A result is the response to a question.
    """

    def __init__(self, data: List[Entity], status: ResultStatus):
        self.data = data
        self.status = status

    @property
    def value(self) -> Entity:
        if self.success() and len(self.data) == 1:
            return self.data[0]
        else:
            raise IndexError("Result is empty")

    def explain(self) -> Any:
        raise NotImplementedError()

    def success(self) -> bool:
        return self.status in [
            ResultStatus.TRUE,
            ResultStatus.FALSE,
            ResultStatus.ANSWERS,
        ]

    def failed(self) -> bool:
        return self.status in [ResultStatus.EMPTY, ResultStatus.ERROR]

    def first(self) -> "Result":
        if self.success():
            return Result(data=[self.data[0]], status=self.status)
        else:
            raise IndexError("Result is empty")

    def __bool__(self) -> bool:
        return self.success()

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        if self.success():
            return iter(self.data)
        else:
            return iter([])

    def __repr__(self) -> str:
        return f"<Result status={self.status}>"


# ------------------------------------------------------------------------
# Question Answering
# ------------------------------------------------------------------------


def ask(
    question: str,
    kg: Optional[KnowledgeGraph] = None,
    model: Optional[WorldAssumption] = WorldAssumption.PARTIAL,
) -> Result:
    """
    Ask a question to the knowledge graph.
    """
    if kg is None:
        kg = Foundation()
        return kg.ask(question)
    else:
        return kg.ask(question)


# ------------------------------------------------------------------------
# Knowledge Graphs
# ------------------------------------------------------------------------


def create_kg(name: str) -> KnowledgeGraph:
    """
    Create a knowledge graph.
    """
    return UserKnowledgeGraph.create(name)


def get_kg(name: str) -> KnowledgeGraph:
    """
    Get a knowledge graph by name.
    """
    rep = req.get_session_name(api_key, name)
    if rep is None:
        raise ValueError(f"Knowledge graph '{name}' does not exist")
    else:
        return UserKnowledgeGraph(rep.id, rep.name)


def ontology(eid: str):
    """
    Return the ontology of the knowledge graph.
    """
    return req.get_ontology(eid)


# ------------------------------------------------------------------------
# Searaching
# ------------------------------------------------------------------------


def find_entity(
    name: str, kg: Optional[KnowledgeGraph] = None, limit: int = 10
) -> Generator[Entity, None, None]:
    """
    Search for entities in the knowledge graph.
    """
    ent = req.get_search_entity(name, limit=limit)
    for e in ent:
        yield Entity(e.id, e.name, e.desc)


def find_relation(
    name: str, kg: Optional[KnowledgeGraph] = None, limit: int = 10
) -> Generator[Relation, None, None]:
    """
    Search for relations in the knowledge graph.
    """
    rel = req.get_search_relation(name)
    for r in rel:
        yield Relation(r.id, r.relation)


def find_triples(
    topic: str, limit: int = 10, kg: Optional[KnowledgeGraph] = None
) -> Generator[Fact, None, None]:
    """
    Return the triples for a given topic.
    """
    graph = req.get_triples(topic, limit=limit)
    for t in graph:
        yield Fact(t.id, t.subject, t.predicate, t.object_)


# ------------------------------------------------------------------------
# Fine Tuning
# ------------------------------------------------------------------------


def fine_tune(file: str) -> str:
    if os.path.exists(file):
        # open the file and get the bytes
        fbody = File(open(file, "rb"))
        rep = req.post_fine_tune(file=fbody)
        return rep.id
    else:
        raise IOError("File does not exist")


# ------------------------------------------------------------------------
# Extraction
# ------------------------------------------------------------------------


def extract_text(
    filename: str,
    model: ExtractModel = ExtractModel.BASE,
    attach: Optional[Entity] = None,
) -> List[Fact]:
    """
    Extract a knowledge graph from a document.
    """
    doc = read_docx(filename)
    body = TextExtract(text=doc, extraction_model=model)
    rep = req.post_extract(body)
    return [Fact(t.id, t.subject, t.predicate, t.object_) for t in rep.triples]
