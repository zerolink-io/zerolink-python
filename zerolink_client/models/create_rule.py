from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_rule_context import CreateRuleContext


T = TypeVar("T", bound="CreateRule")


@_attrs_define
class CreateRule:
    """
    Attributes:
        rule (str): Textual representation of the rule to parse
        context (Union[Unset, CreateRuleContext]): Context of entities to use for parsing the rule
    """

    rule: str
    context: Union[Unset, "CreateRuleContext"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_rule_context import CreateRuleContext

        rule = self.rule

        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_rule_context import CreateRuleContext

        d = src_dict.copy()
        rule = d.pop("rule")

        _context = d.pop("context", UNSET)
        context: Union[Unset, CreateRuleContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = CreateRuleContext.from_dict(_context)

        create_rule = cls(
            rule=rule,
            context=context,
        )

        create_rule.additional_properties = d
        return create_rule

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
