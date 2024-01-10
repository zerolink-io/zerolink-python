from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Candidate")


@_attrs_define
class Candidate:
    """A proposed entity/predicate for a proposed fact.

    Attributes:
        entity (str): User given
        user_defined (bool): Whether the entity is user defined
        entity_id (Union[Unset, str]): The ID of the entity
        suggestion (Union[Unset, str]): Disambiguation suggestion
        description (Union[Unset, str]): Description of the suggestion
    """

    entity: str
    user_defined: bool
    entity_id: Union[Unset, str] = UNSET
    suggestion: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity = self.entity
        user_defined = self.user_defined
        entity_id = self.entity_id
        suggestion = self.suggestion
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
                "user_defined": user_defined,
            }
        )
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity = d.pop("entity")

        user_defined = d.pop("user_defined")

        entity_id = d.pop("entity_id", UNSET)

        suggestion = d.pop("suggestion", UNSET)

        description = d.pop("description", UNSET)

        candidate = cls(
            entity=entity,
            user_defined=user_defined,
            entity_id=entity_id,
            suggestion=suggestion,
            description=description,
        )

        candidate.additional_properties = d
        return candidate

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
