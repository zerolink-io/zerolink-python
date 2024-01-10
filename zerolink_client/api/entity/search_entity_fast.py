from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.match import Match
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    limit: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/entity/{name}/semantic".format(
            name=name,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List["Match"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Match.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List["Match"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 10,
) -> Response[Union[HTTPValidationError, List["Match"]]]:
    """Get Entity Fast

     Search for entity by fast vector nearest neighbor

    Args:
        name (str):
        limit (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Match']]]
    """

    kwargs = _get_kwargs(
        name=name,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 10,
) -> Optional[Union[HTTPValidationError, List["Match"]]]:
    """Get Entity Fast

     Search for entity by fast vector nearest neighbor

    Args:
        name (str):
        limit (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Match']]
    """

    return sync_detailed(
        name=name,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 10,
) -> Response[Union[HTTPValidationError, List["Match"]]]:
    """Get Entity Fast

     Search for entity by fast vector nearest neighbor

    Args:
        name (str):
        limit (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Match']]]
    """

    kwargs = _get_kwargs(
        name=name,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 10,
) -> Optional[Union[HTTPValidationError, List["Match"]]]:
    """Get Entity Fast

     Search for entity by fast vector nearest neighbor

    Args:
        name (str):
        limit (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Match']]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            limit=limit,
        )
    ).parsed
