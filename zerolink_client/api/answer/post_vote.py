from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.downvote_reason import DownvoteReason
from ...models.http_validation_error import HTTPValidationError
from ...models.post_vote_response_post_vote import PostVoteResponsePostVote
from ...types import UNSET, Response


def _get_kwargs(
    *,
    session_id: int,
    rep_id: int,
    code: int,
    reason: DownvoteReason,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["session_id"] = session_id

    params["rep_id"] = rep_id

    params["code"] = code

    json_reason = reason.value
    params["reason"] = json_reason

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/response/vote",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostVoteResponsePostVote.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
    rep_id: int,
    code: int,
    reason: DownvoteReason,
) -> Response[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    """Post Vote

     Vote on a response. Upvote (code=1), downvote (code=-1)

    Args:
        session_id (int):
        rep_id (int):
        code (int):
        reason (DownvoteReason): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PostVoteResponsePostVote]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        rep_id=rep_id,
        code=code,
        reason=reason,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
    rep_id: int,
    code: int,
    reason: DownvoteReason,
) -> Optional[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    """Post Vote

     Vote on a response. Upvote (code=1), downvote (code=-1)

    Args:
        session_id (int):
        rep_id (int):
        code (int):
        reason (DownvoteReason): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PostVoteResponsePostVote]
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        rep_id=rep_id,
        code=code,
        reason=reason,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
    rep_id: int,
    code: int,
    reason: DownvoteReason,
) -> Response[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    """Post Vote

     Vote on a response. Upvote (code=1), downvote (code=-1)

    Args:
        session_id (int):
        rep_id (int):
        code (int):
        reason (DownvoteReason): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PostVoteResponsePostVote]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        rep_id=rep_id,
        code=code,
        reason=reason,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,
    rep_id: int,
    code: int,
    reason: DownvoteReason,
) -> Optional[Union[HTTPValidationError, PostVoteResponsePostVote]]:
    """Post Vote

     Vote on a response. Upvote (code=1), downvote (code=-1)

    Args:
        session_id (int):
        rep_id (int):
        code (int):
        reason (DownvoteReason): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PostVoteResponsePostVote]
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            rep_id=rep_id,
            code=code,
            reason=reason,
        )
    ).parsed
