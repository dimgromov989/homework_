
def get_mask_card_number(mask_card_number: str) -> str:
    """Функция, принимающая на вход номер карты и возвращает ее маску в замаскированном формате"""
    return f"{mask_card_number[0:4]} {mask_card_number[4:6]}** **** {mask_card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в замаскированной форме"""
    return f"**{mask_account[-4:]}"


mask_card_number = input("Введите номер карты:")
mask_account = input("Введите номер счета:")

result = get_mask_card_number(mask_card_number)
result_for_account = get_mask_account(mask_account)

print(result)
print(result_for_account)
