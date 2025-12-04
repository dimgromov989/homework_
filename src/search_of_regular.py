# import json
from collections import Counter
import re


# from pathlib import Path
#
# base_dir = Path(__file__).parent
# data_dir = base_dir / ".." / "data"
#
# path_of_data = data_dir / "operations.json"
#
# with open(path_of_data, mode='r', encoding="utf-8") as file:
#     data = json.load(file)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая принимает список словарей с транзакциями и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    if not search:
        return []
    escaped_search = re.escape(search)
    pattern_of_trans = re.compile(escaped_search, re.IGNORECASE)
    list_for_result = []
    for transaction in data:
        description = transaction.get("description")
        if description and re.search(pattern_of_trans, description):
            list_for_result.append(transaction)

    return list_for_result


# search_query = input("Введите строку поиска: ")
# result = process_bank_search(data, search_query)
# print(result)


categories = [
    "Перевод организации",
    "Открытие вклада",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод с карты на счет",
]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая возвращает словарь,в котором ключи — это названия
    категорий, а значения — это количество операций в каждой категории"""
    if not categories:
        return {}
    descriptions_in_categories = [
        transaction["description"] for transaction in data if transaction.get("description") in categories
    ]
    counts = Counter(descriptions_in_categories)
    return {category: counts.get(category, 0) for category in categories}


# result = process_bank_operations(data, categories)
# print(result)
