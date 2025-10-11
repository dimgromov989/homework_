
list_of_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(list_of_dict: list, state: str) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ соответствует указанному значению."""
    list_for_dict_item = []
    for item_of_dict in list_of_dict:
        for key, value in item_of_dict.items():
            if value == state:
                list_for_dict_item.append(item_of_dict)
    return list_for_dict_item


def sort_by_date(list_of_dict: list, sort: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list_of_date = sorted(list_of_dict, key=lambda x: x['date'], reverse= sort)
    return sorted_list_of_date


result___ = filter_by_state(list_of_dict, state= input() or 'EXECUTED')
result__ = sort_by_date(list_of_dict)

print(f"Фильтр по state: {result___}")
print(f"Фильтр по date:{result__}")











