from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposedFact")


@_attrs_define
class ProposedFact:
    """A propsed triple to be added to the knowledge base.

    Attributes:
        subject (str): The subject of the fact
        predicate (str): The predicate of the fact
        object_ (str): The object of the fact
        saccept (bool): Whether the subject has been accepted
        paccept (bool): Whether the predicate has been accepted
        oaccept (bool): Whether the object has been accepted
        id (Union[Unset, int]): The ID of the fact
    """

    subject: str
    predicate: str
    object_: str
    saccept: bool
    paccept: bool
    oaccept: bool
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        predicate = self.predicate
        object_ = self.object_
        saccept = self.saccept
        paccept = self.paccept
        oaccept = self.oaccept
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "predicate": predicate,
                "object": object_,
                "saccept": saccept,
                "paccept": paccept,
                "oaccept": oaccept,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("subject")

        predicate = d.pop("predicate")

        object_ = d.pop("object")

        saccept = d.pop("saccept")

        paccept = d.pop("paccept")

        oaccept = d.pop("oaccept")

        id = d.pop("id", UNSET)

        proposed_fact = cls(
            subject=subject,
            predicate=predicate,
            object_=object_,
            saccept=saccept,
            paccept=paccept,
            oaccept=oaccept,
            id=id,
        )

        proposed_fact.additional_properties = d
        return proposed_fact

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
