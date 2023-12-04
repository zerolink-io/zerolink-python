from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extract_model import ExtractModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextExtract")


@_attrs_define
class TextExtract:
    """ 
        Attributes:
            text (str): Text to extract from
            extraction_model (Union[Unset, ExtractModel]): An enumeration. Default: ExtractModel.BASE.
     """

    text: str
    extraction_model: Union[Unset, ExtractModel] = ExtractModel.BASE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        extraction_model: Union[Unset, str] = UNSET
        if not isinstance(self.extraction_model, Unset):
            extraction_model = self.extraction_model.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "text": text,
        })
        if extraction_model is not UNSET:
            field_dict["extraction_model"] = extraction_model

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        _extraction_model = d.pop("extraction_model", UNSET)
        extraction_model: Union[Unset, ExtractModel]
        if isinstance(_extraction_model,  Unset):
            extraction_model = UNSET
        else:
            extraction_model = ExtractModel(_extraction_model)




        text_extract = cls(
            text=text,
            extraction_model=extraction_model,
        )

        text_extract.additional_properties = d
        return text_extract

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
