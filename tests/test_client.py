import datetime

import pytest

import zerolink as zl
import zerolink.attribute
import zerolink.req as client


@pytest.fixture
@pytest.mark.skip_ci
def api_key():
    return client.get_user_id()


@pytest.fixture
@pytest.mark.skip_ci
def kg():
    return zl.create_kg("test_kg")


@pytest.mark.skip_ci
def test_create_user(api_key):
    result = client.get_user_id()
    assert result is not None


@pytest.mark.skip_ci
def test_create_kg(api_key):
    zl.api_key = api_key
    result = zl.create_kg("test_kg")
    assert result is not None


@pytest.mark.skip_ci
def test_get_kg(api_key):
    zl.api_key = api_key
    result = zl.get_kg("test_kg")
    assert result is not None


@pytest.mark.skip_ci
def test_create_user_entity(kg):
    e1 = kg.add_entity("Alice", type=zl.EntityType.PERSON)
    assert e1 is not None
    assert e1.id is not None


@pytest.mark.skip_ci
def test_create_user_fact(kg):
    e1 = kg.add_entity("Alice", type=zl.EntityType.PERSON)
    e2 = kg.add_entity("Bob", type=zl.EntityType.ENTITY)
    assert e1 is not None
    assert e2 is not None

    f1 = kg.add_fact(e1, "spouse", e2)
    assert f1 is not None
    assert f1.id is not None

    assert len(kg.entities) >= 2
    assert len(kg.facts) >= 1


@pytest.mark.skip_ci
def test_create_user_entity_types(kg):
    e1 = zl.foundation.entity("Human")
    p1 = zl.foundation.property("instance of")
    e2 = kg.add_entity("Alice", type=e1)
    assert e1 is not None
    assert p1 is not None
    assert e2 is not None


@pytest.mark.skip_ci
def test_entity_search():
    result = list(zl.find_entity("China"))
    assert result is not None
    assert len(result) > 0


@pytest.mark.skip_ci
def test_relation_search():
    result = list(zl.find_relation("place of birth"))
    assert result is not None
    assert len(result) > 0


@pytest.mark.skip_ci
def test_triple_search():
    result = list(zl.find_triples("European Union"))
    assert result is not None
    assert len(result) > 0


@pytest.mark.skip_ci
def test_question(kg):
    result = list(kg.ask("Who are the siblings of George Bush?"))
    assert result is not None
    assert len(result) > 0


@pytest.mark.skip_ci
def test_ontology():
    e1 = zl.foundation.entity("China")
    result = zl.ontology(e1.id)
    assert result is not None
    assert len(result["nodes"]) > 0
    assert len(result["edges"]) > 0
    result2 = e1.ontology()
    assert result2 is not None
    assert len(result["nodes"]) > 0
    assert len(result["edges"]) > 0


@pytest.mark.skip_ci
def test_rules(kg):
    e1 = zl.foundation.entity("China")
    e2 = zl.foundation.entity("Russia")

    ctx = {
        "China": e1,
        "Russia": e2,
    }
    kg.add_rule("China borders Russia", ctx=ctx)


@pytest.mark.skip_ci
def test_attribute(kg):
    e1 = kg.add_entity("Alice", type=zl.EntityType.PERSON)

    # dates
    d0 = datetime.datetime(1946, 7, 6)
    e1.add_attribute("date of birth", d0)

    # gps coordinates
    d1 = zerolink.attribute.gps(latitude=39.9042, longitude=116.4074)
    e1.add_attribute("geolocation", d1)

    # monolingual text
    d2 = "The quick brown fox jumps over the lazy dog."
    e1.add_attribute("motto", d2)

    # integral dimensionless quantity
    d3 = 100_000
    e1.add_attribute("salary", d3)

    # floating point dimensionless quantity
    d4 = 3.1415926
    e1.add_attribute("height", d4)

    # dimensional quantity
    d5 = zerolink.attribute.dimensional_quantity(3.1415926, "meters")
    e1.add_attribute("height", d5)
