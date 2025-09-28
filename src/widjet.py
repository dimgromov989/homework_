from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция реализующая маскировку номера карты/счета с использованием ранее написанных функций"""
    if not user_input.strip():
        return "Ошибка: пустой ввод"
    list_for_words = []
    list_for_digit = []
    new_user_input = user_input.split()
    for item in new_user_input:
        if item.isalpha():
            list_for_words.append(item)
        else:
            list_for_digit.append(item)
    result_for_words = " ".join(list_for_words)
    result_for_digit = "".join(list_for_digit)
    for item_ in new_user_input:
        if item_ == "Счет":
            return f"{result_for_words} {get_mask_account(result_for_digit)}"
        else:
            return f"{result_for_words} {get_mask_card_number(result_for_digit)}"


result_ = mask_account_card(user_input=input("Введите номер карты или счета: "))
print(result_)

