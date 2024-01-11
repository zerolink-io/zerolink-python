from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_cls import ResponseCls
from ..models.response_type import ResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answer_blob import AnswerBlob
    from ..models.candidate_fact import CandidateFact
    from ..models.proposed_fact import ProposedFact


T = TypeVar("T", bound="Rep")


@_attrs_define
class Rep:
    """A response in a chat session.

    Attributes:
        id (int):
        index (int):
        text (str):
        type (ResponseType): An enumeration.
        rep_cls (ResponseCls): An enumeration.
        facts (List['ProposedFact']):
        cfacts (List['CandidateFact']):
        answers (Union[Unset, AnswerBlob]): JSON blob containing the answer to a question and reasoning method used to
            generate the context.
    """

    id: int
    index: int
    text: str
    type: ResponseType
    rep_cls: ResponseCls
    facts: List["ProposedFact"]
    cfacts: List["CandidateFact"]
    answers: Union[Unset, "AnswerBlob"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.answer_blob import AnswerBlob
        from ..models.candidate_fact import CandidateFact
        from ..models.proposed_fact import ProposedFact

        id = self.id

        index = self.index

        text = self.text

        type = self.type.value

        rep_cls = self.rep_cls.value

        facts = []
        for facts_item_data in self.facts:
            facts_item = facts_item_data.to_dict()
            facts.append(facts_item)

        cfacts = []
        for cfacts_item_data in self.cfacts:
            cfacts_item = cfacts_item_data.to_dict()
            cfacts.append(cfacts_item)

        answers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "index": index,
                "text": text,
                "type": type,
                "rep_cls": rep_cls,
                "facts": facts,
                "cfacts": cfacts,
            }
        )
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.answer_blob import AnswerBlob
        from ..models.candidate_fact import CandidateFact
        from ..models.proposed_fact import ProposedFact

        d = src_dict.copy()
        id = d.pop("id")

        index = d.pop("index")

        text = d.pop("text")

        type = ResponseType(d.pop("type"))

        rep_cls = ResponseCls(d.pop("rep_cls"))

        facts = []
        _facts = d.pop("facts")
        for facts_item_data in _facts:
            facts_item = ProposedFact.from_dict(facts_item_data)

            facts.append(facts_item)

        cfacts = []
        _cfacts = d.pop("cfacts")
        for cfacts_item_data in _cfacts:
            cfacts_item = CandidateFact.from_dict(cfacts_item_data)

            cfacts.append(cfacts_item)

        _answers = d.pop("answers", UNSET)
        answers: Union[Unset, AnswerBlob]
        if isinstance(_answers, Unset):
            answers = UNSET
        else:
            answers = AnswerBlob.from_dict(_answers)

        rep = cls(
            id=id,
            index=index,
            text=text,
            type=type,
            rep_cls=rep_cls,
            facts=facts,
            cfacts=cfacts,
            answers=answers,
        )

        rep.additional_properties = d
        return rep

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
