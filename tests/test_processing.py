import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, count_state", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("NONE", 0),
])
def test_filter_by_state(list_of_dict_for_test, state, count_state):
    result = filter_by_state(list_of_dict_for_test, state)
    assert len(result) == count_state


def test_filter_by_state_empty_list(empty_transactions_for_filter):
    result = filter_by_state(empty_transactions_for_filter, 'COMPLETED')
    assert result == []


def test_sort_by_date_empty_list(empty_transactions):
    result = sort_by_date(empty_transactions)
    assert result == []


@pytest.mark.parametrize("sort_flag, expected_ids", [
    (True,  [41428829, 615064591, 594226727, 939719570]),
    (False, [939719570, 594226727, 615064591, 41428829]),
])
def test_sort_by_date_order(list_of_dict_for_test, sort_flag, expected_ids):
    result = sort_by_date(list_of_dict_for_test, sort=sort_flag)
    assert [item["id"] for item in result] == expected_ids







