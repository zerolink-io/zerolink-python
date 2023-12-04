from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proposed_fact import ProposedFact
from ...types import UNSET, Response


def _get_kwargs(
    topic: str,
    *,
    session_id: int,

) -> Dict[str, Any]:
    

    pass


    params: Dict[str, Any] = {}
    params["session_id"] = session_id



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/genfacts/{topic}".format(topic=topic,),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List['ProposedFact']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProposedFact.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List['ProposedFact']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    topic: str,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Response[Union[HTTPValidationError, List['ProposedFact']]]:
    """ Generate Facts

     Generate facts for a topic.

    Args:
        topic (str):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ProposedFact']]]
     """


    kwargs = _get_kwargs(
        topic=topic,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    topic: str,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Optional[Union[HTTPValidationError, List['ProposedFact']]]:
    """ Generate Facts

     Generate facts for a topic.

    Args:
        topic (str):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ProposedFact']]
     """


    return sync_detailed(
        topic=topic,
client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    topic: str,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Response[Union[HTTPValidationError, List['ProposedFact']]]:
    """ Generate Facts

     Generate facts for a topic.

    Args:
        topic (str):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ProposedFact']]]
     """


    kwargs = _get_kwargs(
        topic=topic,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    topic: str,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Optional[Union[HTTPValidationError, List['ProposedFact']]]:
    """ Generate Facts

     Generate facts for a topic.

    Args:
        topic (str):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ProposedFact']]
     """


    return (await asyncio_detailed(
        topic=topic,
client=client,
session_id=session_id,

    )).parsed
