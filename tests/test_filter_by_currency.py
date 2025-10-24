import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("JPY", []),
    ],
)
def test_filter_by_currency(sample_transactions, currency, expected_ids):
    filtered = list(filter_by_currency(sample_transactions, currency))
    assert [t["id"] for t in filtered] == expected_ids


def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_invalid_currency():
    transactions = [{"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(filter_by_currency(transactions, "")) == []
    assert list(filter_by_currency(transactions, None)) == []
