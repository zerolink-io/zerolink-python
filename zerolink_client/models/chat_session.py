import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rep import Rep
    from ..models.req import Req


T = TypeVar("T", bound="ChatSession")


@_attrs_define
class ChatSession:
    """A user chat session.

    Attributes:
        id (int):
        name (str): The name of the chat session
        index (int):
        requests (List['Req']):
        responses (List['Rep']):
        created_on (datetime.datetime):
    """

    id: int
    name: str
    index: int
    requests: List["Req"]
    responses: List["Rep"]
    created_on: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.rep import Rep
        from ..models.req import Req

        id = self.id

        name = self.name

        index = self.index

        requests = []
        for requests_item_data in self.requests:
            requests_item = requests_item_data.to_dict()
            requests.append(requests_item)

        responses = []
        for responses_item_data in self.responses:
            responses_item = responses_item_data.to_dict()
            responses.append(responses_item)

        created_on = self.created_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "index": index,
                "requests": requests,
                "responses": responses,
                "created_on": created_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rep import Rep
        from ..models.req import Req

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        index = d.pop("index")

        requests = []
        _requests = d.pop("requests")
        for requests_item_data in _requests:
            requests_item = Req.from_dict(requests_item_data)

            requests.append(requests_item)

        responses = []
        _responses = d.pop("responses")
        for responses_item_data in _responses:
            responses_item = Rep.from_dict(responses_item_data)

            responses.append(responses_item)

        created_on = isoparse(d.pop("created_on"))

        chat_session = cls(
            id=id,
            name=name,
            index=index,
            requests=requests,
            responses=responses,
            created_on=created_on,
        )

        chat_session.additional_properties = d
        return chat_session

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
