from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.waitlist_response import WaitlistResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
    email: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["name"] = name

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/waitlist",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, WaitlistResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WaitlistResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, WaitlistResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    email: str,
) -> Response[Union[HTTPValidationError, WaitlistResponse]]:
    """Post Waitlist

     Add email to waitlist

    Args:
        name (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, WaitlistResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    email: str,
) -> Optional[Union[HTTPValidationError, WaitlistResponse]]:
    """Post Waitlist

     Add email to waitlist

    Args:
        name (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, WaitlistResponse]
    """

    return sync_detailed(
        client=client,
        name=name,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    email: str,
) -> Response[Union[HTTPValidationError, WaitlistResponse]]:
    """Post Waitlist

     Add email to waitlist

    Args:
        name (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, WaitlistResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    email: str,
) -> Optional[Union[HTTPValidationError, WaitlistResponse]]:
    """Post Waitlist

     Add email to waitlist

    Args:
        name (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, WaitlistResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            email=email,
        )
    ).parsed
