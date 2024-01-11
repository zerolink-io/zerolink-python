from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.candidate_fact import CandidateFact


T = TypeVar("T", bound="AssertionResponse")


@_attrs_define
class AssertionResponse:
    """A response to an fact request.

    Attributes:
        id (str): The ID of the assertion
        msg (str): A message describing the result of the assertion
        inappropriate (bool): Whether the given content violates the content policy
        cfacts (List['CandidateFact']): The candidate facts.
    """

    id: str
    msg: str
    inappropriate: bool
    cfacts: List["CandidateFact"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.candidate_fact import CandidateFact

        id = self.id

        msg = self.msg

        inappropriate = self.inappropriate

        cfacts = []
        for cfacts_item_data in self.cfacts:
            cfacts_item = cfacts_item_data.to_dict()
            cfacts.append(cfacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "msg": msg,
                "inappropriate": inappropriate,
                "cfacts": cfacts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.candidate_fact import CandidateFact

        d = src_dict.copy()
        id = d.pop("id")

        msg = d.pop("msg")

        inappropriate = d.pop("inappropriate")

        cfacts = []
        _cfacts = d.pop("cfacts")
        for cfacts_item_data in _cfacts:
            cfacts_item = CandidateFact.from_dict(cfacts_item_data)

            cfacts.append(cfacts_item)

        assertion_response = cls(
            id=id,
            msg=msg,
            inappropriate=inappropriate,
            cfacts=cfacts,
        )

        assertion_response.additional_properties = d
        return assertion_response

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
