import json
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    r"C:\Users\user\PycharmProjects\homework\logs\utils.log", mode="w", encoding="utf-8"
)
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

file_path = r"C:\Users\user\PycharmProjects\homework\data\operations.json"


def data_for_transactions(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info(
            "Принимается путь до JSON-файла и возвращается список словарей с данными о финансовых транзакциях."
        )
        with open(file_path, encoding="utf-8") as file:
            transactions = json.load(file)
            logger.info("Процесс сравнения транзакций с заданным типом.")
            if not isinstance(transactions, list):
                logger.warning("Транзакция не содержит список.")
                return []
        logger.debug("Тип соответствует заданному, возращение транзакции ")
        return transactions
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Произошла ошибка: {ex}.")
        return []

# result = data_for_transactions(file_path)
# print(result)
