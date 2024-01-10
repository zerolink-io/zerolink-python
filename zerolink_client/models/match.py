from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Match")


@_attrs_define
class Match:
    """
    Attributes:
        name (str):
        id (Union[Unset, str]):
        desc (Union[Unset, str]):
        score (Union[Unset, float]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        desc = self.desc
        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if desc is not UNSET:
            field_dict["desc"] = desc
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        desc = d.pop("desc", UNSET)

        score = d.pop("score", UNSET)

        match = cls(
            name=name,
            id=id,
            desc=desc,
            score=score,
        )

        match.additional_properties = d
        return match

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
