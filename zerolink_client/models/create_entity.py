from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEntity")


@_attrs_define
class CreateEntity:
    """
    Attributes:
        entity (str): Name of entity
        entity_type (Union[Unset, EntityType]): Entity types are entities that map to base ontological entities in
            Foundation.
        entity_str (Union[Unset, str]): User specified type
        is_class (Union[Unset, bool]): Whether the entity is a class or instance
    """

    entity: str
    entity_type: Union[Unset, EntityType] = UNSET
    entity_str: Union[Unset, str] = UNSET
    is_class: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity = self.entity
        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        entity_str = self.entity_str
        is_class = self.is_class

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
            }
        )
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity_str is not UNSET:
            field_dict["entity_str"] = entity_str
        if is_class is not UNSET:
            field_dict["is_class"] = is_class

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity = d.pop("entity")

        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, EntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = EntityType(_entity_type)

        entity_str = d.pop("entity_str", UNSET)

        is_class = d.pop("is_class", UNSET)

        create_entity = cls(
            entity=entity,
            entity_type=entity_type,
            entity_str=entity_str,
            is_class=is_class,
        )

        create_entity.additional_properties = d
        return create_entity

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
