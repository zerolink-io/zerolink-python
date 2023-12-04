from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assertion_response import AssertionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.proposed_fact import ProposedFact
from ...types import UNSET, Response


def _get_kwargs(
    *,
    json_body: List['ProposedFact'],
    session_id: int,

) -> Dict[str, Any]:
    

    pass


    params: Dict[str, Any] = {}
    params["session_id"] = session_id



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)






    

    return {
        "method": "post",
        "url": "/genfacts/accept",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssertionResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],
    session_id: int,

) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    """ Accept Facts

     Accept generated facts

    Args:
        session_id (int):
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssertionResponse, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],
    session_id: int,

) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    """ Accept Facts

     Accept generated facts

    Args:
        session_id (int):
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssertionResponse, HTTPValidationError]
     """


    return sync_detailed(
        client=client,
json_body=json_body,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],
    session_id: int,

) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    """ Accept Facts

     Accept generated facts

    Args:
        session_id (int):
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssertionResponse, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],
    session_id: int,

) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    """ Accept Facts

     Accept generated facts

    Args:
        session_id (int):
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssertionResponse, HTTPValidationError]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
session_id=session_id,

    )).parsed
