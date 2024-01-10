from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tune_job_response import CreateTuneJobResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, File, FileJsonType, Response


def _get_kwargs(
    *,
    file: Union[File, str],
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_file: Union[FileJsonType, str]

    if isinstance(file, File):
        json_file = file.to_tuple()

    else:
        json_file = file

    params["file"] = json_file

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/finetune",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CreateTuneJobResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateTuneJobResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CreateTuneJobResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[File, str],
) -> Response[Union[CreateTuneJobResponse, HTTPValidationError]]:
    """Fine Tuning

     Fine-tune the model with the provided data

    Args:
        file (Union[File, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTuneJobResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[File, str],
) -> Optional[Union[CreateTuneJobResponse, HTTPValidationError]]:
    """Fine Tuning

     Fine-tune the model with the provided data

    Args:
        file (Union[File, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTuneJobResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        file=file,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[File, str],
) -> Response[Union[CreateTuneJobResponse, HTTPValidationError]]:
    """Fine Tuning

     Fine-tune the model with the provided data

    Args:
        file (Union[File, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTuneJobResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[File, str],
) -> Optional[Union[CreateTuneJobResponse, HTTPValidationError]]:
    """Fine Tuning

     Fine-tune the model with the provided data

    Args:
        file (Union[File, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTuneJobResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            file=file,
        )
    ).parsed
