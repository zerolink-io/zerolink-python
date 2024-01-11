from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Relation")


@_attrs_define
class Relation:
    """
    Attributes:
        id (str):
        relation (str):
        description (Union[Unset, str]):
        source (Union[Unset, str]):
        source_id (Union[Unset, str]):
        source_url (Union[Unset, str]):
    """

    id: str
    relation: str
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        relation = self.relation

        description = self.description

        source = self.source

        source_id = self.source_id

        source_url = self.source_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "relation": relation,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        relation = d.pop("relation")

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        source_id = d.pop("source_id", UNSET)

        source_url = d.pop("source_url", UNSET)

        relation = cls(
            id=id,
            relation=relation,
            description=description,
            source=source,
            source_id=source_id,
            source_url=source_url,
        )

        relation.additional_properties = d
        return relation

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
