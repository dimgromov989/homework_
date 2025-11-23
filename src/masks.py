import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'C:\Users\user\PycharmProjects\homework\logs\masks.log', mode='w', encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(mask_card_number: str) -> str:
    """Функция, принимающая на вход номер карты и возвращает ее маску в замаскированном формате"""
    logger.info('Принимается номер карты')
    if not mask_card_number:
        logger.warning('Не введен номер карты')
        return "Номер карты отсутствует"
    elif len(mask_card_number) < 16 or len(mask_card_number) > 16:
        logger.error(f'Введен не верный формат номера карты: {mask_card_number}')
        return "Неверный формат номера карты"
    logger.info('Возвращение маски карты в замаскированном виде')
    return f"{mask_card_number[0:4]} {mask_card_number[4:6]}** **** {mask_card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в замаскированной форме"""
    if not mask_account:
        logger.warning("Переданный счет пуст.")
        return "Номер счета отсутствует"
    elif len(mask_account) != 20:
        logger.error(f"Счет '{mask_account}' имеет неверный формат. Длина должна быть ровно 20 символов.")
        return "Неверный формат номера счета"
    else:
        masked_value = f"**{mask_account[-4:]}"
        logger.debug(f"Успешно замаскирован счет '{mask_account}'. Результат: {masked_value}")
        return masked_value

 # mask_card_number = input("Введите номер карты:")
 # mask_account = input("Введите номер счета:")

# result = get_mask_card_number(mask_card_number)
# result_for_account = get_mask_account(mask_account)

# print(result)
# print(result_for_account)
