from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_entity import CreateEntity
from ...models.create_entity_response import CreateEntityResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    json_body: CreateEntity,
    session_id: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["session_id"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/userentity",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CreateEntityResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateEntityResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CreateEntityResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateEntity,
    session_id: int,
) -> Response[Union[CreateEntityResponse, HTTPValidationError]]:
    """Post User Entity

     Add an user-defined entity to a session.

    Args:
        session_id (int):
        json_body (CreateEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEntityResponse, HTTPValidationError]]
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
    json_body: CreateEntity,
    session_id: int,
) -> Optional[Union[CreateEntityResponse, HTTPValidationError]]:
    """Post User Entity

     Add an user-defined entity to a session.

    Args:
        session_id (int):
        json_body (CreateEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEntityResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateEntity,
    session_id: int,
) -> Response[Union[CreateEntityResponse, HTTPValidationError]]:
    """Post User Entity

     Add an user-defined entity to a session.

    Args:
        session_id (int):
        json_body (CreateEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEntityResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CreateEntity,
    session_id: int,
) -> Optional[Union[CreateEntityResponse, HTTPValidationError]]:
    """Post User Entity

     Add an user-defined entity to a session.

    Args:
        session_id (int):
        json_body (CreateEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEntityResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            session_id=session_id,
        )
    ).parsed
