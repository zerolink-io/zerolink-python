from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_type import RequestType

T = TypeVar("T", bound="Req")


@_attrs_define
class Req:
    """ A request in a chat session.

        Attributes:
            id (int):
            index (int):
            text (str):
            type (RequestType): An enumeration.
     """

    id: int
    index: int
    text: str
    type: RequestType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        index = self.index
        text = self.text
        type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "index": index,
            "text": text,
            "type": type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        index = d.pop("index")

        text = d.pop("text")

        type = RequestType(d.pop("type"))




        req = cls(
            id=id,
            index=index,
            text=text,
            type=type,
        )

        req.additional_properties = d
        return req

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
