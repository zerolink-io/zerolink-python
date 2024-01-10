from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_entity import GenericEntity


T = TypeVar("T", bound="GenericTriple")


@_attrs_define
class GenericTriple:
    """
    Attributes:
        id (str):
        subject (GenericEntity):
        predicate (str):
        object_ (GenericEntity):
    """

    id: str
    subject: "GenericEntity"
    predicate: str
    object_: "GenericEntity"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.generic_entity import GenericEntity

        id = self.id
        subject = self.subject.to_dict()

        predicate = self.predicate
        object_ = self.object_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subject": subject,
                "predicate": predicate,
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.generic_entity import GenericEntity

        d = src_dict.copy()
        id = d.pop("id")

        subject = GenericEntity.from_dict(d.pop("subject"))

        predicate = d.pop("predicate")

        object_ = GenericEntity.from_dict(d.pop("object"))

        generic_triple = cls(
            id=id,
            subject=subject,
            predicate=predicate,
            object_=object_,
        )

        generic_triple.additional_properties = d
        return generic_triple

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
