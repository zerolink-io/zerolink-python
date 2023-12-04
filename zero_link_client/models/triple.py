from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Triple")


@_attrs_define
class Triple:
    """ 
        Attributes:
            subject (str): The subject of the triple
            object_ (str): The object of the triple
            predicate (str): The predicate of the triple
            id (Union[Unset, str]):
     """

    subject: str
    object_: str
    predicate: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        object_ = self.object_
        predicate = self.predicate
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subject": subject,
            "object": object_,
            "predicate": predicate,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("subject")

        object_ = d.pop("object")

        predicate = d.pop("predicate")

        id = d.pop("id", UNSET)

        triple = cls(
            subject=subject,
            object_=object_,
            predicate=predicate,
            id=id,
        )

        triple.additional_properties = d
        return triple

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
