from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType

if TYPE_CHECKING:
  from ..models.date import Date
  from ..models.datetime_ import Datetime
  from ..models.dimensional_quantity import DimensionalQuantity
  from ..models.dimensionless_quantity import DimensionlessQuantity
  from ..models.gps import GPS
  from ..models.monolingual_text import MonolingualText
  from ..models.url import URL





T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """ 
        Attributes:
            type (AttributeType): An enumeration.
            value (Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText',
                'URL']):
     """

    type: AttributeType
    value: Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText', 'URL']
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.date import Date
        from ..models.datetime_ import Datetime
        from ..models.dimensional_quantity import DimensionalQuantity
        from ..models.dimensionless_quantity import DimensionlessQuantity
        from ..models.gps import GPS
        from ..models.monolingual_text import MonolingualText
        type = self.type.value

        value: Dict[str, Any]

        if isinstance(self.value, MonolingualText):
            value = self.value.to_dict()

        elif isinstance(self.value, GPS):
            value = self.value.to_dict()

        elif isinstance(self.value, Date):
            value = self.value.to_dict()

        elif isinstance(self.value, Datetime):
            value = self.value.to_dict()

        elif isinstance(self.value, DimensionlessQuantity):
            value = self.value.to_dict()

        elif isinstance(self.value, DimensionalQuantity):
            value = self.value.to_dict()

        else:
            value = self.value.to_dict()




        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date import Date
        from ..models.datetime_ import Datetime
        from ..models.dimensional_quantity import DimensionalQuantity
        from ..models.dimensionless_quantity import DimensionlessQuantity
        from ..models.gps import GPS
        from ..models.monolingual_text import MonolingualText
        from ..models.url import URL
        d = src_dict.copy()
        type = AttributeType(d.pop("type"))




        def _parse_value(data: object) -> Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText', 'URL']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = MonolingualText.from_dict(data)



                return value_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = GPS.from_dict(data)



                return value_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = Date.from_dict(data)



                return value_type_2
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_3 = Datetime.from_dict(data)



                return value_type_3
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_4 = DimensionlessQuantity.from_dict(data)



                return value_type_4
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_5 = DimensionalQuantity.from_dict(data)



                return value_type_5
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            value_type_6 = URL.from_dict(data)



            return value_type_6

        value = _parse_value(d.pop("value"))


        attribute = cls(
            type=type,
            value=value,
        )

        attribute.additional_properties = d
        return attribute

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
