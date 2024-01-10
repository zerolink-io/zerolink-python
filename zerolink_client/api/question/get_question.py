from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rep import Rep
from ...types import UNSET, Response


def _get_kwargs(
    question_id: int,
    *,
    session_id: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["session_id"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/question/{question_id}".format(
            question_id=question_id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, Rep]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Rep.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, Rep]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    question_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Response[Union[HTTPValidationError, Rep]]:
    """Get Question

    Args:
        question_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Rep]]
    """

    kwargs = _get_kwargs(
        question_id=question_id,
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    question_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Optional[Union[HTTPValidationError, Rep]]:
    """Get Question

    Args:
        question_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Rep]
    """

    return sync_detailed(
        question_id=question_id,
        client=client,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    question_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Response[Union[HTTPValidationError, Rep]]:
    """Get Question

    Args:
        question_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Rep]]
    """

    kwargs = _get_kwargs(
        question_id=question_id,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    question_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Optional[Union[HTTPValidationError, Rep]]:
    """Get Question

    Args:
        question_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Rep]
    """

    return (
        await asyncio_detailed(
            question_id=question_id,
            client=client,
            session_id=session_id,
        )
    ).parsed
