import pytest

from generators import transaction_descriptions


def test_transaction_descriptions(sample_transactions):
    """Тест вида операции"""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected


def test_transaction_descriptions_empty_list():
    """Тест на пустой список"""
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_missing_key():
    """Тест на отсутствие ключа description"""
    transactions = [{"id": 1}, {"description": "Перевод со счета на счет"}]
    with pytest.raises(KeyError):
        list(transaction_descriptions(transactions))


def test_transaction_descriptions_single():
    """Тест на один элемент"""
    transactions = [{"description": "Только одно"}]
    assert list(transaction_descriptions(transactions)) == ["Только одно"]
