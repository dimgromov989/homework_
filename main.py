from src.csv_excel_reader import reader_for_csv, path_of_csv, reader_for_excel, path_of_excel
from src.processing import filter_by_state, sort_by_date
from src.search_of_regular import process_bank_search
from src.utils import data_for_transactions, file_path


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")
    def process_user_input(input_for_information):
        handlers = {
            1: ("JSON-файл", lambda: data_for_transactions(file_path)),
            2: ("CSV-файл", lambda: reader_for_csv(path_of_csv)),
            3: ("XLSX-файл", lambda: reader_for_excel(path_of_excel))
        }
        handler = handlers.get(input_for_information)
        if handler is None:
            print("Введены некорректные данные")
            return None
        file_type, func = handler
        print(f"Для обработки выбран {file_type}.")
        return func()

    input_for_information = int(input("Выберите нужный вариант: "))
    result = process_user_input(input_for_information)

    while True:
        input_for_status = input("Введите статус, по которому необходимо выполнить фильтрацию\n"
                                 "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper().strip()
        if input_for_status in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        else:
            print(f"\nСтатус '{input_for_status}' недоступен. Попробуйте снова.\n")
    result_after_filter_of_state = filter_by_state(result, input_for_status)
    print(f"Операции отфильтрованы по статусу: {input_for_status}")

    def sorted_date_for_result(result_after_filter_of_state):
        print("Отсортировать операции по дате? Да/Нет")
        user_input_date = input("Введите ваш выбор: ").strip().lower()
        if user_input_date == "да":
            user_input_date_decreasing = input("Введите ваш выбор (по возрастанию / по убыванию): ").strip().lower()
            if user_input_date_decreasing == "по возрастанию":
                result_after_sort_date_true = sort_by_date(result_after_filter_of_state, False)
                return result_after_sort_date_true
            elif user_input_date_decreasing == "по убыванию":
                result_after_sort_date_false = sort_by_date(result_after_filter_of_state, True)
                return result_after_sort_date_false
        else:
            return result_after_filter_of_state

    result_for_sorted_date = sorted_date_for_result(result_after_filter_of_state)

    print("Выводить только рублевые транзакции? Да/Нет")
    def transaction_of_rub(result_for_sorted_date):
        list_for_result = []
        user_input_for_rub = input("Введите ваш выбор: ").strip().lower()
        if user_input_for_rub == "да":
            for transaction in result_for_sorted_date:
                if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
                    list_for_result.append(transaction)
            return list_for_result
        else:
            return result_for_sorted_date

    result_of_rub = transaction_of_rub(result_for_sorted_date)

    def sort_of_reg(result_of_rub):
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input_sort_reg_yes = input("Введите ваш выбор: ").strip().lower()
        if user_input_sort_reg_yes == "да":
            user_input_sort_reg = input("Введите строку поиска: ").strip().lower()
            result_for_search = process_bank_search(result_of_rub, user_input_sort_reg)
            return result_for_search
        else:
            return result_of_rub

    result_for_sort_reg = sort_of_reg(result_of_rub)

    if result_for_sort_reg:
        print(f"Всего банковских операций в выборке: {len(result_for_sort_reg)}")
        for index, transaction in enumerate(result_for_sort_reg, start=1):
            date = transaction["date"]
            description = transaction["description"]
            account_from = transaction.get("from", "")
            account_to = transaction.get("to", "")
            amount = transaction["operationAmount"]["amount"] if isinstance(transaction.get("operationAmount"), dict) else ""
            currency = transaction["operationAmount"].get("currency", {}).get("code", "") if isinstance(transaction.get("operationAmount"), dict) else ""

            formatted_amount = f"Сумма: {amount} {currency}" if amount else ""
            accounts = f"{account_from} -> {account_to}" if account_from or account_to else ""

            print(f"""
                {index}. Дата: {date}
                Описание: {description}
                {'Счета:' if accounts else ''}{accounts}
                {formatted_amount}
                   """)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()