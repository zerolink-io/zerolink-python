from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTriple")


@_attrs_define
class CreateTriple:
    """
    Attributes:
        predicate (str): Name of predicate relation
        user_subject (Union[Unset, str]): EID of a user entity
        subject (Union[Unset, str]): EID of a builtin entity
        user_object (Union[Unset, str]): EID of a user entity
        object_ (Union[Unset, str]): EID of a builtin entity
    """

    predicate: str
    user_subject: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    user_object: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicate = self.predicate
        user_subject = self.user_subject
        subject = self.subject
        user_object = self.user_object
        object_ = self.object_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "predicate": predicate,
            }
        )
        if user_subject is not UNSET:
            field_dict["user_subject"] = user_subject
        if subject is not UNSET:
            field_dict["subject"] = subject
        if user_object is not UNSET:
            field_dict["user_object"] = user_object
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        predicate = d.pop("predicate")

        user_subject = d.pop("user_subject", UNSET)

        subject = d.pop("subject", UNSET)

        user_object = d.pop("user_object", UNSET)

        object_ = d.pop("object", UNSET)

        create_triple = cls(
            predicate=predicate,
            user_subject=user_subject,
            subject=subject,
            user_object=user_object,
            object_=object_,
        )

        create_triple.additional_properties = d
        return create_triple

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
