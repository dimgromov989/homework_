import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("mask_card_number, encrypted_for_card",[
    ("7000792389608361", "7000 79** **** 8361"),
    ("", "Номер карты отсутствует"),
    ("956165", "Неверный формат номера карты")
    ])
def test_get_mask_card_number(mask_card_number, encrypted_for_card):
    assert get_mask_card_number(mask_card_number) == encrypted_for_card


@pytest.mark.parametrize("mask_account, encrypted_for_account",[
    ("73654108430135874305", "**4305"),
    ("546", "Неверный формат номера счета"),
    ("", "Номер счета отсутствует"),
    ("549651", "Неверный формат номера счета")
    ])
def test_get_mask_account(mask_account, encrypted_for_account):
    assert get_mask_account(mask_account) == encrypted_for_account



