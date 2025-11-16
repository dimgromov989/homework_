import requests
import json
import os
from dotenv import load_dotenv


def currency_conversion(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
     в рублях, тип данных — float"""
    load_dotenv()
    if 'operationAmount' in transaction:
        if transaction.get('operationAmount').get('currency').get('code') == 'RUB':
            amount_for_rub = transaction.get('operationAmount').get('amount')
            return float(amount_for_rub)
        elif transaction.get('operationAmount').get('currency').get('code') in ['USD', 'EUR']:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "amount": f"{transaction.get('operationAmount').get('amount')}",
                "from": f"{transaction.get('operationAmount').get('currency').get('code')}",
                "to": "RUB"
            }
            api_key = os.getenv("API_KEY")
            headers = {
                "apikey": api_key
            }
            response = requests.get(url, headers=headers, params=payload)
            result_of_json = response.json()
            result_amount = result_of_json['result']
            return result_amount
    else:
        return 'Нет суммы транзакции'


result = currency_conversion(transaction={
    "id": 41428875,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
})

print(result)
