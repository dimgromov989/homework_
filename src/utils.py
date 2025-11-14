import json


file_path = r'C:\Users\user\PycharmProjects\homework\data\operations.json'

def data_for_transactions(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
        и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, encoding='utf-8') as file:
            transactions = json.load(file)
            if not isinstance(transactions, list):
                return []
        return transactions
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# result = data_for_transactions(file_path)
# print(result)

