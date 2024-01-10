from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph import Graph


T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """
    Attributes:
        id (str):
        entity (str):
        description (Union[Unset, str]):
        source (Union[Unset, str]):
        source_url (Union[Unset, str]):
        ontology (Union[Unset, Graph]):
        source_id (Union[Unset, str]):
    """

    id: str
    entity: str
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    ontology: Union[Unset, "Graph"] = UNSET
    source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.graph import Graph

        id = self.id
        entity = self.entity
        description = self.description
        source = self.source
        source_url = self.source_url
        ontology: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ontology, Unset):
            ontology = self.ontology.to_dict()

        source_id = self.source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entity": entity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if ontology is not UNSET:
            field_dict["ontology"] = ontology
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.graph import Graph

        d = src_dict.copy()
        id = d.pop("id")

        entity = d.pop("entity")

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        source_url = d.pop("source_url", UNSET)

        _ontology = d.pop("ontology", UNSET)
        ontology: Union[Unset, Graph]
        if isinstance(_ontology, Unset):
            ontology = UNSET
        else:
            ontology = Graph.from_dict(_ontology)

        source_id = d.pop("source_id", UNSET)

        entity = cls(
            id=id,
            entity=entity,
            description=description,
            source=source,
            source_url=source_url,
            ontology=ontology,
            source_id=source_id,
        )

        entity.additional_properties = d
        return entity

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
