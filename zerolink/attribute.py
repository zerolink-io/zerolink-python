import datetime
from typing import Any

from zerolink_client.models import (
    GPS,
    URL,
    Attribute,
    AttributeType,
    Date,
    Datetime,
    DimensionalQuantity,
    DimensionlessQuantity,
    MonolingualText,
)

__all__ = ["url", "gps", "quantity", "value"]


def url(x: str) -> URL:
    """
    Create a URL object.

    Examples:

    >>> url("https://www.google.com")
    """
    return URL(x)


def gps(latitude: float, longitude: float) -> GPS:
    """
    Create a GPS coordinate object.

    Examples:

    >>> gps(39.9042, 116.4074)
    """
    return GPS(latitude=latitude, longitude=longitude)


def quantity(value: float, unit: str) -> DimensionalQuantity:
    """
    Unit is either a string of a formula of SI units. Or an EID number of an
    entity to use as the unit (i.e. people, products, etc.)

    Examples:

    >>> quantity(1.0, "meter")
    >>> quantity(2.0, "human")
    >>> quantity(3.0, "meter / second")
    """
    if isinstance(value, int):
        val = DimensionlessQuantity(value=str(value), integer=True)
    elif isinstance(value, float):
        val = DimensionlessQuantity(value=str(value), integer=False)
    return DimensionalQuantity(value=val, unit=unit)


def value(x: Any) -> Attribute:
    """
    Create an Attribute object polymorphically.

    Examples:

    >>> value("The quick brown fox jumps over the lazy dog.")
    >>> value(100_000)
    >>> value(3.1415926)
    >>> value(gps(39.9042, 116.4074))
    >>> value(url("https://www.google.com"))
    >>> value(datetime.date(1946, 7, 6))
    >>> value(datetime(2019, 5, 18, 15, 17, 8, 132263))
    >>> value(quantity(1.0, "meter"))
    """
    if isinstance(x, str):
        v0 = MonolingualText(language="en", text=x)
        return Attribute(type=AttributeType.MONOLINGUAL_TEXT, value=v0)
    elif isinstance(x, int):
        v1 = DimensionlessQuantity(value=str(x), integer=True)
        return Attribute(type=AttributeType.DIMENSIONLESS_QUANTITY, value=v1)
    elif isinstance(x, float):
        v2 = DimensionlessQuantity(value=str(x), integer=False)
        return Attribute(type=AttributeType.DIMENSIONLESS_QUANTITY, value=v2)
    elif isinstance(x, DimensionalQuantity):
        v3 = DimensionalQuantity(value=x.value, unit=x.unit)
        return Attribute(type=AttributeType.DIMENSIONAL_QUANTITY, value=v3)
    elif isinstance(x, GPS):
        return Attribute(type=AttributeType.GPS_COORDINATES, value=x)
    elif isinstance(x, URL):
        return Attribute(type=AttributeType.URL, value=x)
    elif isinstance(x, datetime.date):
        d0 = Date(date=x)
        return Attribute(type=AttributeType.DATE, value=d0)
    elif isinstance(x, datetime.datetime):
        d1 = Datetime(datetime_=x)
        return Attribute(type=AttributeType.DATETIME, value=d1)
    else:
        raise Exception("Unknown attribute type: " + str(type(x)))
