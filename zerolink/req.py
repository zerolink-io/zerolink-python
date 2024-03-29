from typing import Any, Optional, cast

from zerolink import settings
from zerolink.exc import APIError, AuthenticationError
from zerolink_client import Client
from zerolink_client.api.default import finetune, get_models_models_get
from zerolink_client.api.entity import (
    desc_entity_id,
    desc_entity_ontology,
    lookup_entity,
    lookup_relation,
    search_entity,
)
from zerolink_client.api.extract import extract_text
from zerolink_client.api.fact import (
    create_userattribute,
    create_userentity,
    create_userrule,
    create_usertriple,
)
from zerolink_client.api.kg import get_triple
from zerolink_client.api.question import post_question
from zerolink_client.api.session import (
    create_session,
    get_session_entities,
    get_session_facts,
    get_user_session,
)
from zerolink_client.api.user import create_user
from zerolink_client.models import (
    ChatSession,
    CreateAttribute,
    CreateEntity,
    CreateRule,
    CreateRuleResponse,
    CreateTriple,
    CreateTuneJobResponse,
    Entity,
    HTTPValidationError,
    Question,
    QuestionResponse,
    TextExtract,
)
from zerolink_client.types import File, UNSET

# ------------------------------------------------------------------------
# Endpoints
# ------------------------------------------------------------------------

client = Client(
    base_url=settings.server_url,
    raise_on_unexpected_status=False,
)


def check_api_key() -> None:
    """
    Check if the API key is set.
    """
    if settings.api_key is None:
        raise AuthenticationError()
    else:
        pass


def get_user_id() -> str:
    """
    Get the user ID from the server. Only used for Demo server.
    """
    client._headers["Authorization"] = settings.api_key
    rep = create_user.sync(client=client)
    if rep is None:
        raise Exception("Failed to authenticate.")
    settings.api_key = rep.user_id
    if isinstance(rep, HTTPValidationError):
        raise APIError(str(rep))
    return rep.user_id


def post_session(user_id: str, **kwargs) -> Optional[ChatSession]:
    """
    Create a new session.
    """
    check_api_key()
    if user_id is None:
        user_id = settings.api_key
    rep = create_session.sync(client=client, user_id=user_id, **kwargs)
    if isinstance(rep, HTTPValidationError):
        raise APIError(str(rep))
    return rep


def get_session_name(user_id: str, session_name: str, **kwargs):
    """
    Lookup a session by user and name.
    """
    check_api_key()
    rep = get_user_session.sync_detailed(user_id, session_name, client=client, **kwargs)
    if rep.status_code == 200:
        return rep.parsed
    elif rep.status_code == 404:
        return None
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_session_entities_list(session_id: int, **kwargs):
    """
    Get the entities of a session.
    """
    check_api_key()
    rep = get_session_entities.sync_detailed(session_id, client=client, **kwargs)
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_session_facts_list(session_id: int, **kwargs):
    """
    Get the facts of a session.
    """
    check_api_key()
    rep = get_session_facts.sync_detailed(session_id, client=client, **kwargs)
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def ask_question(
    session_id: Optional[int],
    body: str,
    assumps: Optional[dict[str, Any]] = None,
    **kwargs,
) -> QuestionResponse:
    """
    Ask a question.
    """
    check_api_key()
    rep = post_question.sync_detailed(
        client=client,
        session_id=(session_id or UNSET),
        body=Question(body=body, **(assumps or {})),
        **kwargs,
    )
    if rep.status_code == 200:
        return cast(QuestionResponse, rep.parsed)
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_entity_id(id: str, **kwargs) -> Entity:
    """
    Get the description of an entity by eid.
    """
    check_api_key()
    rep = desc_entity_id.sync_detailed(
        client=client,
        id=id,
        **kwargs,
    )
    if rep.status_code == 200:
        return cast(Entity, rep.parsed)
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_desc_entity(name: str, **kwargs):
    """
    Get the description of an entity by eid.
    """
    check_api_key()
    rep = lookup_entity.sync_detailed(
        client=client,
        name=name,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_search_entity(name: str, **kwargs):
    """
    Search for an entity.
    """
    check_api_key()
    rep = search_entity.sync_detailed(
        client=client,
        name=name,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_search_relation(name: str, **kwargs):
    """
    Search for a relation.
    """
    check_api_key()
    rep = lookup_relation.sync_detailed(
        client=client,
        name=name,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_ontology(name: str, **kwargs) -> dict[str, Any]:
    """
    Get the ontology of an entity.
    """
    check_api_key()
    rep = desc_entity_ontology.sync_detailed(
        client=client,
        id=name,
        **kwargs,
    )
    if rep.status_code == 200:
        return cast(dict[str, Any], rep.parsed)
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_triples(name: str, **kwargs):
    """
    Get the triples of a session.
    """
    check_api_key()
    rep = get_triple.sync_detailed(
        client=client,
        name=name,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def get_reasoners(name: str, **kwargs):
    """
    Get the reasoners available.
    """
    check_api_key()
    rep = get_models_models_get.sync_detailed(
        client=client,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)


def add_entity(session_id: int, body: CreateEntity, **kwargs):
    """
    Add a user entity to a session.
    """
    check_api_key()
    rep = create_userentity.sync_detailed(
        client=client,
        session_id=session_id,
        body=body,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        print(err)
        raise APIError(err)


def add_triple(session_id: int, body: CreateTriple, **kwargs):
    """
    Add a user triple to a session.
    """
    check_api_key()
    rep = create_usertriple.sync_detailed(
        client=client,
        session_id=session_id,
        body=body,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)


def add_attribute(session_id: int, body: CreateAttribute, **kwargs):
    """
    Add a user attribute to a session.
    """
    check_api_key()
    rep = create_userattribute.sync_detailed(
        client=client,
        session_id=session_id,
        body=body,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)


def post_rule(session_id: int, body: CreateRule, **kwargs) -> CreateRuleResponse:
    """
    Add a user rule to a session.
    """
    check_api_key()
    rep = create_userrule.sync_detailed(
        client=client,
        session_id=session_id,
        body=body,
        **kwargs,
    )
    if rep.status_code == 200:
        return cast(CreateRuleResponse, rep.parsed)
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)


def post_extract(body: TextExtract, **kwargs):
    """
    Extract text from a document.
    """
    check_api_key()
    rep = extract_text.sync_detailed(
        client=client,
        body=body,
        **kwargs,
    )
    if rep.status_code == 200:
        return rep.parsed
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)


def post_fine_tune(file: File, **kwargs) -> CreateTuneJobResponse:
    """
    Upload data to to create a fine-tuning job.
    """
    check_api_key()
    # kwargs['files'] = {'file': file}
    rep = finetune.sync_detailed(
        client=client,
        file=file,
        **kwargs,
    )
    if rep.status_code == 200:
        return cast(CreateTuneJobResponse, rep.parsed)
    else:
        err = rep.content.decode("utf-8")
        raise APIError(err)
