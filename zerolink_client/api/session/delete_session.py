from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_session_response_delete_session import DeleteSessionResponseDeleteSession
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    session_id: int,
) -> Dict[str, Any]:
    return {
        "method": "delete",
        "url": "/session/{session_id}".format(
            session_id=session_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteSessionResponseDeleteSession.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
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
) -> Response[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
    """Delete Session

     Delete a session.

    Args:
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
    """Delete Session

     Delete a session.

    Args:
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSessionResponseDeleteSession, HTTPValidationError]
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
    """Delete Session

     Delete a session.

    Args:
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DeleteSessionResponseDeleteSession, HTTPValidationError]]:
    """Delete Session

     Delete a session.

    Args:
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSessionResponseDeleteSession, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
        )
    ).parsed
