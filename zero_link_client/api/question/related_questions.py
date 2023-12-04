from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proposed_fact import ProposedFact
from ...types import Response


def _get_kwargs(
    *,
    json_body: List['ProposedFact'],

) -> Dict[str, Any]:
    

    pass


    

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)






    

    return {
        "method": "post",
        "url": "/related_questions/",
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List[str]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],

) -> Response[Union[HTTPValidationError, List[str]]]:
    """ Related Questions

     Get related questions for a set of facts.

    Args:
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[str]]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],

) -> Optional[Union[HTTPValidationError, List[str]]]:
    """ Related Questions

     Get related questions for a set of facts.

    Args:
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[str]]
     """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],

) -> Response[Union[HTTPValidationError, List[str]]]:
    """ Related Questions

     Get related questions for a set of facts.

    Args:
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[str]]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List['ProposedFact'],

) -> Optional[Union[HTTPValidationError, List[str]]]:
    """ Related Questions

     Get related questions for a set of facts.

    Args:
        json_body (List['ProposedFact']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[str]]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
