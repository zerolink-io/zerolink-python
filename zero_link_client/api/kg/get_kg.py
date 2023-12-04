from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.graph import Graph
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: int,
    *,
    topic: Union[Unset, None, str] = UNSET,
    threshold: Union[Unset, None, float] = 0.4,

) -> Dict[str, Any]:
    

    pass


    params: Dict[str, Any] = {}
    params["topic"] = topic


    params["threshold"] = threshold



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/session/{session_id}/kg".format(session_id=session_id,),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Graph, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Graph.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Graph, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, None, str] = UNSET,
    threshold: Union[Unset, None, float] = 0.4,

) -> Response[Union[Graph, HTTPValidationError]]:
    """ Get Kg

     Get the knowledge graph for a given session.

    Args:
        session_id (int):
        topic (Union[Unset, None, str]):
        threshold (Union[Unset, None, float]):  Default: 0.4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Graph, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
topic=topic,
threshold=threshold,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, None, str] = UNSET,
    threshold: Union[Unset, None, float] = 0.4,

) -> Optional[Union[Graph, HTTPValidationError]]:
    """ Get Kg

     Get the knowledge graph for a given session.

    Args:
        session_id (int):
        topic (Union[Unset, None, str]):
        threshold (Union[Unset, None, float]):  Default: 0.4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Graph, HTTPValidationError]
     """


    return sync_detailed(
        session_id=session_id,
client=client,
topic=topic,
threshold=threshold,

    ).parsed

async def asyncio_detailed(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, None, str] = UNSET,
    threshold: Union[Unset, None, float] = 0.4,

) -> Response[Union[Graph, HTTPValidationError]]:
    """ Get Kg

     Get the knowledge graph for a given session.

    Args:
        session_id (int):
        topic (Union[Unset, None, str]):
        threshold (Union[Unset, None, float]):  Default: 0.4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Graph, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
topic=topic,
threshold=threshold,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, None, str] = UNSET,
    threshold: Union[Unset, None, float] = 0.4,

) -> Optional[Union[Graph, HTTPValidationError]]:
    """ Get Kg

     Get the knowledge graph for a given session.

    Args:
        session_id (int):
        topic (Union[Unset, None, str]):
        threshold (Union[Unset, None, float]):  Default: 0.4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Graph, HTTPValidationError]
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
topic=topic,
threshold=threshold,

    )).parsed
