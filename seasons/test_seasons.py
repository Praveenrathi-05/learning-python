import pytest
from seasons import validate_date


def test_valid_date():
    assert str(validate_date("2000-01-01")) == "2000-01-01"


def test_invalid_month():
    with pytest.raises(ValueError):
        validate_date("2000-13-01")


def test_invalid_day():
    with pytest.raises(ValueError):
        validate_date("2000-02-30")


def test_invalid_format():
    with pytest.raises(ValueError):
        validate_date("January 1, 2000")
