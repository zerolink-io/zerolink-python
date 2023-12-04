from zero_link_client.models import (
    EntityType,
    SpatialAssumption,
    TemporalAssumption,
    WorldAssumption,
)
from zerolink.api import (
    ask,
    create_kg,
    extract_text,
    find_entity,
    find_relation,
    find_triples,
    fine_tune,
    get_kg,
    ontology,
)
from zerolink.exc import APIError
from zerolink.extract import read_docx
from zerolink.foundation import foundation
from zerolink.req import get_desc_entity, get_user_id
from zerolink.settings import read_api_key

api_key = read_api_key()

__all__ = [
    "foundation",
    "api_key",
    "ask",
    "create_kg",
    "get_kg",
    "find_entity",
    "find_relation",
    "find_triples",
    "ontology",
    "get_user_id",
    "get_desc_entity",
    "read_docx",
    "fine_tune",
    "extract_text",
    "APIError",
    "EntityType",
    "SpatialAssumption",
    "TemporalAssumption",
    "WorldAssumption",
]
