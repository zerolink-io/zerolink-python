from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.explanation import Explanation
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    response_id: int,
    answer_id: int,
    *,
    session_id: int,

) -> Dict[str, Any]:
    

    pass


    params: Dict[str, Any] = {}
    params["session_id"] = session_id



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "method": "get",
        "url": "/explain/{response_id}/{answer_id}".format(response_id=response_id,answer_id=answer_id,),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Explanation, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Explanation.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Explanation, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    response_id: int,
    answer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Response[Union[Explanation, HTTPValidationError]]:
    """ Explain Answer

    Args:
        response_id (int):
        answer_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Explanation, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        response_id=response_id,
answer_id=answer_id,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    response_id: int,
    answer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Optional[Union[Explanation, HTTPValidationError]]:
    """ Explain Answer

    Args:
        response_id (int):
        answer_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Explanation, HTTPValidationError]
     """


    return sync_detailed(
        response_id=response_id,
answer_id=answer_id,
client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    response_id: int,
    answer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Response[Union[Explanation, HTTPValidationError]]:
    """ Explain Answer

    Args:
        response_id (int):
        answer_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Explanation, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        response_id=response_id,
answer_id=answer_id,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    response_id: int,
    answer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    session_id: int,

) -> Optional[Union[Explanation, HTTPValidationError]]:
    """ Explain Answer

    Args:
        response_id (int):
        answer_id (int):
        session_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Explanation, HTTPValidationError]
     """


    return (await asyncio_detailed(
        response_id=response_id,
answer_id=answer_id,
client=client,
session_id=session_id,

    )).parsed
