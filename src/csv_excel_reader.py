import pandas
import json
import pandas as pd


path_of_csv = r'C:\Users\user\Downloads\transactions.csv'

def reader_for_csv(path_of_csv):
    """Функция предназначена для чтения файлов формата csv"""
    dataframe_of_csv = pd.read_csv(path_of_csv)
    return dataframe_of_csv.to_json(orient='records')

res = reader_for_csv(path_of_csv)
# print(res)
path_of_excel = r'C:\Users\user\Downloads\transactions_excel.xlsx'

def reader_for_excel(path_of_excel):
    """Функция предназначена для чтения файлов формата excel"""
    dataframe_of_excel = pd.read_excel(path_of_excel)
    return dataframe_of_excel.to_json(orient='records')

result = reader_for_excel(path_of_excel)
# print(result)










