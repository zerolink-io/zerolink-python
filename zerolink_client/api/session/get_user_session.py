from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_session import ChatSession
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    user_id: str,
    session_name: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/user/{user_id}/session/{session_name}".format(
            user_id=user_id,
            session_name=session_name,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChatSession, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChatSession.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChatSession, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    session_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ChatSession, HTTPValidationError]]:
    """Get Session By Name

     Get a session by name.

    Args:
        user_id (str):
        session_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatSession, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        session_name=session_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    session_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ChatSession, HTTPValidationError]]:
    """Get Session By Name

     Get a session by name.

    Args:
        user_id (str):
        session_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatSession, HTTPValidationError]
    """

    return sync_detailed(
        user_id=user_id,
        session_name=session_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    session_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ChatSession, HTTPValidationError]]:
    """Get Session By Name

     Get a session by name.

    Args:
        user_id (str):
        session_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatSession, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        session_name=session_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    session_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ChatSession, HTTPValidationError]]:
    """Get Session By Name

     Get a session by name.

    Args:
        user_id (str):
        session_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatSession, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            session_name=session_name,
            client=client,
        )
    ).parsed
