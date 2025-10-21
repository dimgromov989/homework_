import pytest

@pytest.fixture
def mask_card_number():
    return [
    ("7000792389608361", "7000 79** **** 8361"),
    ("", "Номер карты отсутствует"),
    ("956165", "Неверный формат номера карты")
    ]


@pytest.fixture
def mask_account():
    return [
    ("73654108430135874305", "**4305"),
    ("546", "Неверный формат номера счета"),
    ("", "Номер счета отсутствует"),
    ("549651", "Неверный формат номера счета")
    ]


@pytest.fixture
def list_of_dict_for_test():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

@pytest.fixture
def empty_transactions_for_filter():
    return []

@pytest.fixture
def empty_transactions():
    return []


@pytest.fixture
def invalid_inputs():
    return [
        "",
        "   ",
        "abc",
        "Счет",
        "Visa Classic",
        "Card 12345",
        "Счет abc",
        "1234567890124566",
    ]

@pytest.fixture
def valid_card_inputs():
    return [
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("MasterCard 1596837868705199", "MasterCard 1596 83** **** 5199"),
        ("Maestro 7158300734726758", "Maestro 7158 30** **** 6758"),
    ]

@pytest.fixture
def valid_account_inputs_for_account():
    return [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счёт 98765432109876543210", "Счёт **3210"),
    ]




