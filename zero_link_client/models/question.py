from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.context_assumption import ContextAssumption
from ..models.spatial_assumption import SpatialAssumption
from ..models.temporal_assumption import TemporalAssumption
from ..models.world_assumption import WorldAssumption
from ..types import UNSET, Unset

T = TypeVar("T", bound="Question")


@_attrs_define
class Question:
    """ A question to be answered by querying the knowledge graph and reasoner.

        Attributes:
            body (str): The body of the question
            world (Union[Unset, WorldAssumption]): The world assumption is the assumption about the world that the reasoner
                makes. This is used to determine the answer to a query. For example, if
                the world assumption is "closed" then the reasoner will assume that the
                answer to the query is "no" if it cannot find a triple to satisfy the
                query. Default: WorldAssumption.CLOSED.
            spatial (Union[Unset, SpatialAssumption]): The spatial assumption is the assumption about space that the
                reasoner
                makes. This is used to determine the answer to a query. For example, if the
                spatial assumption is "earth" then the reasoner will only consider
                geographic locations on Earth and will assume all instances of 'location'
                are on Earth. If the spatial assumption is "universe" then the reasoner
                then this restriction is lifted and the reasoner will consider all
                locations in the universe. Default: SpatialAssumption.EARTH.
            temporal (Union[Unset, TemporalAssumption]): The temporal assumption is the assumption about time that the
                reasoner
                makes. This is used to determine the answer to a query. For example, if
                the temporal assumption is "current" then the reasoner will only consider
                triples that refer to entities that are non-historical. Excluding things
                like the Roman Empire and Francoist Spain. Default: TemporalAssumption.CURRENT.
            context (Union[Unset, ContextAssumption]): The context assumption is the assumption about the context that the
                reasoner makes. This is used to determine the answer to a query. For
                example, if the context assumption is "none" then the reasoner will only
                consider basic triples like instance_of and subclass_of. If the context
                assumption is "local" then the reasoner will consider triples that are
                defined by the user. If the context assumption is "global" then the
                reasoner will consider all queryable triples. Default: ContextAssumption.GLOBAL.
     """

    body: str
    world: Union[Unset, WorldAssumption] = WorldAssumption.CLOSED
    spatial: Union[Unset, SpatialAssumption] = SpatialAssumption.EARTH
    temporal: Union[Unset, TemporalAssumption] = TemporalAssumption.CURRENT
    context: Union[Unset, ContextAssumption] = ContextAssumption.GLOBAL
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        world: Union[Unset, str] = UNSET
        if not isinstance(self.world, Unset):
            world = self.world.value

        spatial: Union[Unset, str] = UNSET
        if not isinstance(self.spatial, Unset):
            spatial = self.spatial.value

        temporal: Union[Unset, str] = UNSET
        if not isinstance(self.temporal, Unset):
            temporal = self.temporal.value

        context: Union[Unset, str] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "body": body,
        })
        if world is not UNSET:
            field_dict["world"] = world
        if spatial is not UNSET:
            field_dict["spatial"] = spatial
        if temporal is not UNSET:
            field_dict["temporal"] = temporal
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        _world = d.pop("world", UNSET)
        world: Union[Unset, WorldAssumption]
        if isinstance(_world,  Unset):
            world = UNSET
        else:
            world = WorldAssumption(_world)




        _spatial = d.pop("spatial", UNSET)
        spatial: Union[Unset, SpatialAssumption]
        if isinstance(_spatial,  Unset):
            spatial = UNSET
        else:
            spatial = SpatialAssumption(_spatial)




        _temporal = d.pop("temporal", UNSET)
        temporal: Union[Unset, TemporalAssumption]
        if isinstance(_temporal,  Unset):
            temporal = UNSET
        else:
            temporal = TemporalAssumption(_temporal)




        _context = d.pop("context", UNSET)
        context: Union[Unset, ContextAssumption]
        if isinstance(_context,  Unset):
            context = UNSET
        else:
            context = ContextAssumption(_context)




        question = cls(
            body=body,
            world=world,
            spatial=spatial,
            temporal=temporal,
            context=context,
        )

        question.additional_properties = d
        return question

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
