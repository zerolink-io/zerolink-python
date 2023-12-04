from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

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
            value (Union[Unset, Any]):
            value_type (Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText',
                'URL', Unset]):
     """

    type: AttributeType
    value: Union[Unset, Any] = UNSET
    value_type: Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText', 'URL', Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.date import Date
        from ..models.datetime_ import Datetime
        from ..models.dimensional_quantity import DimensionalQuantity
        from ..models.dimensionless_quantity import DimensionlessQuantity
        from ..models.gps import GPS
        from ..models.monolingual_text import MonolingualText
        type = self.type.value

        value = self.value
        value_type: Union[Dict[str, Any], Unset]
        if isinstance(self.value_type, Unset):
            value_type = UNSET

        elif isinstance(self.value_type, MonolingualText):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        elif isinstance(self.value_type, GPS):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        elif isinstance(self.value_type, Date):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        elif isinstance(self.value_type, Datetime):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        elif isinstance(self.value_type, DimensionlessQuantity):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        elif isinstance(self.value_type, DimensionalQuantity):
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()

        else:
            value_type = UNSET
            if not isinstance(self.value_type, Unset):
                value_type = self.value_type.to_dict()




        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
        })
        if value is not UNSET:
            field_dict["value"] = value
        if value_type is not UNSET:
            field_dict["value_type"] = value_type

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




        value = d.pop("value", UNSET)

        def _parse_value_type(data: object) -> Union['Date', 'Datetime', 'DimensionalQuantity', 'DimensionlessQuantity', 'GPS', 'MonolingualText', 'URL', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_0 = data
                value_type_type_0: Union[Unset, MonolingualText]
                if isinstance(_value_type_type_0,  Unset):
                    value_type_type_0 = UNSET
                else:
                    value_type_type_0 = MonolingualText.from_dict(_value_type_type_0)



                return value_type_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_1 = data
                value_type_type_1: Union[Unset, GPS]
                if isinstance(_value_type_type_1,  Unset):
                    value_type_type_1 = UNSET
                else:
                    value_type_type_1 = GPS.from_dict(_value_type_type_1)



                return value_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_2 = data
                value_type_type_2: Union[Unset, Date]
                if isinstance(_value_type_type_2,  Unset):
                    value_type_type_2 = UNSET
                else:
                    value_type_type_2 = Date.from_dict(_value_type_type_2)



                return value_type_type_2
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_3 = data
                value_type_type_3: Union[Unset, Datetime]
                if isinstance(_value_type_type_3,  Unset):
                    value_type_type_3 = UNSET
                else:
                    value_type_type_3 = Datetime.from_dict(_value_type_type_3)



                return value_type_type_3
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_4 = data
                value_type_type_4: Union[Unset, DimensionlessQuantity]
                if isinstance(_value_type_type_4,  Unset):
                    value_type_type_4 = UNSET
                else:
                    value_type_type_4 = DimensionlessQuantity.from_dict(_value_type_type_4)



                return value_type_type_4
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_type_5 = data
                value_type_type_5: Union[Unset, DimensionalQuantity]
                if isinstance(_value_type_type_5,  Unset):
                    value_type_type_5 = UNSET
                else:
                    value_type_type_5 = DimensionalQuantity.from_dict(_value_type_type_5)



                return value_type_type_5
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _value_type_type_6 = data
            value_type_type_6: Union[Unset, URL]
            if isinstance(_value_type_type_6,  Unset):
                value_type_type_6 = UNSET
            else:
                value_type_type_6 = URL.from_dict(_value_type_type_6)



            return value_type_type_6

        value_type = _parse_value_type(d.pop("value_type", UNSET))


        attribute = cls(
            type=type,
            value=value,
            value_type=value_type,
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
