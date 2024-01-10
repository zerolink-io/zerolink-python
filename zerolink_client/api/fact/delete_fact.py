from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_fact_response_delete_fact import DeleteFactResponseDeleteFact
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    fact_id: int,
    *,
    session_id: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["session_id"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/fact/{fact_id}".format(
            fact_id=fact_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteFactResponseDeleteFact.from_dict(response.json())

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
) -> Response[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Response[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    """Delete Fact

    Args:
        fact_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        fact_id=fact_id,
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Optional[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    """Delete Fact

    Args:
        fact_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteFactResponseDeleteFact, HTTPValidationError]
    """

    return sync_detailed(
        fact_id=fact_id,
        client=client,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    fact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Response[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    """Delete Fact

    Args:
        fact_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        fact_id=fact_id,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
) -> Optional[Union[DeleteFactResponseDeleteFact, HTTPValidationError]]:
    """Delete Fact

    Args:
        fact_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteFactResponseDeleteFact, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            fact_id=fact_id,
            client=client,
            session_id=session_id,
        )
    ).parsed
