from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute


T = TypeVar("T", bound="CreateAttribute")


@_attrs_define
class CreateAttribute:
    """
    Attributes:
        subject (str): EID of a builtin entity
        predicate (str): Name of attribute
        attribute (Attribute):
    """

    subject: str
    predicate: str
    attribute: "Attribute"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.attribute import Attribute

        subject = self.subject
        predicate = self.predicate
        attribute = self.attribute.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "predicate": predicate,
                "attribute": attribute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute import Attribute

        d = src_dict.copy()
        subject = d.pop("subject")

        predicate = d.pop("predicate")

        attribute = Attribute.from_dict(d.pop("attribute"))

        create_attribute = cls(
            subject=subject,
            predicate=predicate,
            attribute=attribute,
        )

        create_attribute.additional_properties = d
        return create_attribute

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
