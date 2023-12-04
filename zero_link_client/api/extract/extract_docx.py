from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assertion_response import AssertionResponse
from ...models.body_extract_docx import BodyExtractDocx
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    multipart_data: BodyExtractDocx,
    session_id: int,

) -> Dict[str, Any]:
    

    pass


    params: Dict[str, Any] = {}
    params["session_id"] = session_id



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    multipart_multipart_data = multipart_data.to_multipart()




    return {
        "method": "post",
        "url": "/extract/docx",
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssertionResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyExtractDocx,
    session_id: int,

) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    """ Extract Docx

     Extract text from a docx file

    Args:
        session_id (int):
        multipart_data (BodyExtractDocx):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssertionResponse, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        multipart_data=multipart_data,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyExtractDocx,
    session_id: int,

) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    """ Extract Docx

     Extract text from a docx file

    Args:
        session_id (int):
        multipart_data (BodyExtractDocx):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssertionResponse, HTTPValidationError]
     """


    return sync_detailed(
        client=client,
multipart_data=multipart_data,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyExtractDocx,
    session_id: int,

) -> Response[Union[AssertionResponse, HTTPValidationError]]:
    """ Extract Docx

     Extract text from a docx file

    Args:
        session_id (int):
        multipart_data (BodyExtractDocx):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssertionResponse, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        multipart_data=multipart_data,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyExtractDocx,
    session_id: int,

) -> Optional[Union[AssertionResponse, HTTPValidationError]]:
    """ Extract Docx

     Extract text from a docx file

    Args:
        session_id (int):
        multipart_data (BodyExtractDocx):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssertionResponse, HTTPValidationError]
     """


    return (await asyncio_detailed(
        client=client,
multipart_data=multipart_data,
session_id=session_id,

    )).parsed
