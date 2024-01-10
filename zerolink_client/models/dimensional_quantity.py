from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensionless_quantity import DimensionlessQuantity


T = TypeVar("T", bound="DimensionalQuantity")


@_attrs_define
class DimensionalQuantity:
    """
    Attributes:
        value (DimensionlessQuantity):
        unit (str):
    """

    value: "DimensionlessQuantity"
    unit: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dimensionless_quantity import DimensionlessQuantity

        value = self.value.to_dict()

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensionless_quantity import DimensionlessQuantity

        d = src_dict.copy()
        value = DimensionlessQuantity.from_dict(d.pop("value"))

        unit = d.pop("unit")

        dimensional_quantity = cls(
            value=value,
            unit=unit,
        )

        dimensional_quantity.additional_properties = d
        return dimensional_quantity

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
