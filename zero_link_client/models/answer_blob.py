from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnswerBlob")


@_attrs_define
class AnswerBlob:
    """ JSON blob containing the answer to a question and reasoning method used to
    generate the context.

        Attributes:
            answers (List[str]): The answer(s) to the question
            methods (List[str]): The methods used to derive the answer
     """

    answers: List[str]
    methods: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        answers = self.answers




        methods = self.methods





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "answers": answers,
            "methods": methods,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        answers = cast(List[str], d.pop("answers"))


        methods = cast(List[str], d.pop("methods"))


        answer_blob = cls(
            answers=answers,
            methods=methods,
        )

        answer_blob.additional_properties = d
        return answer_blob

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
