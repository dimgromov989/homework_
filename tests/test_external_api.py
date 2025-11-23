from unittest.mock import patch, Mock
from src.external_api import currency_conversion
import os
from dotenv import load_dotenv

def test_currency_conversion_usd_success():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"rate": 81.186179},
        "date": "2025-11-14",
        "result": 667461.616445
    }

    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = currency_conversion(transaction)

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": f"{api_key}"},
        params={
            "amount": "8221.37",
            "from": "USD",
            "to": "RUB"
        }
    )

    expected =  667461.616445

    assert result == expected


def test_currency_conversion_rub():
    transaction = {
        "operationAmount": {
            "amount": "5000.00",
            "currency": {"code": "RUB"}
        }
    }
    result = currency_conversion(transaction)
    assert result == 5000.0


def test_currency_conversion_no_operation_amount():
    transaction = {"id": 123}
    result = currency_conversion(transaction)
    assert result == "Нет суммы транзакции"
