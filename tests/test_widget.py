import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("MasterCard 1596837868705199", "MasterCard 1596 83** **** 5199"),
        ("Maestro 7158300734726758", "Maestro 7158 30** **** 6758"),
    ],
)
def test_mask_account_card_card(valid_card_inputs, input_str, expected):
    result = mask_account_card(input_str)
    assert result == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счёт 98765432109876543210", "Счёт **3210"),
    ],
)
def test_mask_account_card_account(input_str, expected):
    result = mask_account_card(input_str)
    assert result == expected


def test_mask_account_card_empty_input(invalid_inputs):
    result = mask_account_card("")
    assert result == "Ошибка: пустой ввод"
    result = mask_account_card("   ")
    assert result == "Ошибка: пустой ввод"
