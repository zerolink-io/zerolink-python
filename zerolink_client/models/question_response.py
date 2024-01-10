from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.result_status import ResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_response_query import QuestionResponseQuery


T = TypeVar("T", bound="QuestionResponse")


@_attrs_define
class QuestionResponse:
    """A response to a question request.

    Attributes:
        id (int): The ID of the question
        msg (str): A message describing the result of the question
        status (ResultStatus): The status of a result.
        answers (List[str]): The answers to the question
        methods (List[str]): The methods used to answer the question
        reasoners (List[str]): The reasoners used to answer the question
        query (Union[Unset, QuestionResponseQuery]): The query used to answer the question
    """

    id: int
    msg: str
    status: ResultStatus
    answers: List[str]
    methods: List[str]
    reasoners: List[str]
    query: Union[Unset, "QuestionResponseQuery"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.question_response_query import QuestionResponseQuery

        id = self.id
        msg = self.msg
        status = self.status.value

        answers = self.answers

        methods = self.methods

        reasoners = self.reasoners

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "msg": msg,
                "status": status,
                "answers": answers,
                "methods": methods,
                "reasoners": reasoners,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_response_query import QuestionResponseQuery

        d = src_dict.copy()
        id = d.pop("id")

        msg = d.pop("msg")

        status = ResultStatus(d.pop("status"))

        answers = cast(List[str], d.pop("answers"))

        methods = cast(List[str], d.pop("methods"))

        reasoners = cast(List[str], d.pop("reasoners"))

        _query = d.pop("query", UNSET)
        query: Union[Unset, QuestionResponseQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = QuestionResponseQuery.from_dict(_query)

        question_response = cls(
            id=id,
            msg=msg,
            status=status,
            answers=answers,
            methods=methods,
            reasoners=reasoners,
            query=query,
        )

        question_response.additional_properties = d
        return question_response

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
