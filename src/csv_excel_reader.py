from pathlib import Path

import pandas as pd


base_dir = Path(__file__).parent
data_dir = base_dir / ".." / "data"

path_of_csv = data_dir / "transactions.csv"
path_of_excel = data_dir / "transactions_excel.xlsx"


def reader_for_csv(path_of_csv):
    """Читает CSV-файл и возвращает список транзакций в формате, совместимом с JSON."""
    df = pd.read_csv(path_of_csv, sep=";")
    records = df.to_dict(orient="records")
    normalized = []
    for r in records:
        normalized.append({
            "id": r.get("id"),
            "state": r.get("state"),
            "date": r.get("date"),
            "operationAmount": {
                "amount": str(r.get("amount", "")),
                "currency": {
                    "name": r.get("currency_name", ""),
                    "code": r.get("currency_code", "")
                }
            },
            "description": r.get("description", ""),
            "from": r.get("from", ""),
            "to": r.get("to", "")
        })
    return normalized

# res = reader_for_csv(path_of_csv)
# print(res)


def reader_for_excel(path_of_excel):
    """Читает Excel-файл и возвращает список транзакций в формате, совместимом с JSON."""
    df = pd.read_excel(path_of_excel)
    records = df.to_dict(orient="records")
    normalized = []
    for r in records:
        normalized.append({
            "id": r.get("id"),
            "state": r.get("state"),
            "date": r.get("date"),
            "operationAmount": {
                "amount": str(r.get("amount", "")),
                "currency": {
                    "name": r.get("currency_name", ""),
                    "code": r.get("currency_code", "")
                }
            },
            "description": r.get("description", ""),
            "from": r.get("from", ""),
            "to": r.get("to", "")
        })
    return normalized


# result = reader_for_excel(path_of_excel)
# print(result)
