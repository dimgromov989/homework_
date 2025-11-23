from pathlib import Path

import pandas as pd


base_dir = Path(__file__).parent
data_dir = base_dir / ".." / "data"

path_of_csv = data_dir / "transactions.csv"
path_of_excel = data_dir / "transactions_excel.xlsx"


def reader_for_csv(path_of_csv):
    """Функция предназначена для чтения файлов формата csv"""
    dataframe_of_csv = pd.read_csv(path_of_csv)
    return dataframe_of_csv.to_json(orient="records")


# res = reader_for_csv(path_of_csv)
# print(res)


def reader_for_excel(path_of_excel):
    """Функция предназначена для чтения файлов формата excel"""
    dataframe_of_excel = pd.read_excel(path_of_excel)
    return dataframe_of_excel.to_json(orient="records")


# result = reader_for_excel(path_of_excel)
# print(result)
