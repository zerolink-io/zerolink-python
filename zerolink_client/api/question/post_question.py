from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.question import Question
from ...models.question_response import QuestionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Question,
    session_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["session_id"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/question",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, QuestionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QuestionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, QuestionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Question,
    session_id: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, QuestionResponse]]:
    r"""Post Question

     This is the main entry point for the knowledge graph question answering
    system and is used by the \"ask\" command in the client library.

    * world : The world assumption to use for the question. Open World
        Assumption (OWA), Closed World Assumption (CWA), or Partial Closed
        World Assumption (PCWA). Defaults to PCWA.
    * temporal : The temporal assumption to use for the question. Current,
        Historical, or Abstract. Defaults to Current.
    * spatial : The spatial assumption to use for the question. Earth or
        Universe. Defaults to Earth.
    * context : The context assumption to use for the question. None, Local,
        or Global. Defaults to Local.
    * quest : The question to answer.
    * session_id : The session to answer the question in.

    Args:
        session_id (Union[Unset, int]):
        body (Question): A question to be answered by querying the knowledge graph and reasoner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QuestionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Question,
    session_id: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, QuestionResponse]]:
    r"""Post Question

     This is the main entry point for the knowledge graph question answering
    system and is used by the \"ask\" command in the client library.

    * world : The world assumption to use for the question. Open World
        Assumption (OWA), Closed World Assumption (CWA), or Partial Closed
        World Assumption (PCWA). Defaults to PCWA.
    * temporal : The temporal assumption to use for the question. Current,
        Historical, or Abstract. Defaults to Current.
    * spatial : The spatial assumption to use for the question. Earth or
        Universe. Defaults to Earth.
    * context : The context assumption to use for the question. None, Local,
        or Global. Defaults to Local.
    * quest : The question to answer.
    * session_id : The session to answer the question in.

    Args:
        session_id (Union[Unset, int]):
        body (Question): A question to be answered by querying the knowledge graph and reasoner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QuestionResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Question,
    session_id: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, QuestionResponse]]:
    r"""Post Question

     This is the main entry point for the knowledge graph question answering
    system and is used by the \"ask\" command in the client library.

    * world : The world assumption to use for the question. Open World
        Assumption (OWA), Closed World Assumption (CWA), or Partial Closed
        World Assumption (PCWA). Defaults to PCWA.
    * temporal : The temporal assumption to use for the question. Current,
        Historical, or Abstract. Defaults to Current.
    * spatial : The spatial assumption to use for the question. Earth or
        Universe. Defaults to Earth.
    * context : The context assumption to use for the question. None, Local,
        or Global. Defaults to Local.
    * quest : The question to answer.
    * session_id : The session to answer the question in.

    Args:
        session_id (Union[Unset, int]):
        body (Question): A question to be answered by querying the knowledge graph and reasoner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QuestionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Question,
    session_id: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, QuestionResponse]]:
    r"""Post Question

     This is the main entry point for the knowledge graph question answering
    system and is used by the \"ask\" command in the client library.

    * world : The world assumption to use for the question. Open World
        Assumption (OWA), Closed World Assumption (CWA), or Partial Closed
        World Assumption (PCWA). Defaults to PCWA.
    * temporal : The temporal assumption to use for the question. Current,
        Historical, or Abstract. Defaults to Current.
    * spatial : The spatial assumption to use for the question. Earth or
        Universe. Defaults to Earth.
    * context : The context assumption to use for the question. None, Local,
        or Global. Defaults to Local.
    * quest : The question to answer.
    * session_id : The session to answer the question in.

    Args:
        session_id (Union[Unset, int]):
        body (Question): A question to be answered by querying the knowledge graph and reasoner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QuestionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            session_id=session_id,
        )
    ).parsed
