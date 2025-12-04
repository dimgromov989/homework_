import pandas as pd


def reader_for_csv(path):
    """Читает CSV-файл и возвращает список транзакций в формате, совместимом с JSON."""
    df = pd.read_csv(path, sep=";")
    records = df.to_dict(orient="records")
    normalized = []
    for r in records:
        normalized.append(
            {
                "id": r.get("id"),
                "state": r.get("state"),
                "date": r.get("date"),
                "operationAmount": {
                    "amount": str(r.get("amount", "")),
                    "currency": {"name": r.get("currency_name", ""), "code": r.get("currency_code", "")},
                },
                "description": r.get("description", ""),
                "from": r.get("from", ""),
                "to": r.get("to", ""),
            }
        )
    return normalized


# res = reader_for_csv(path_of_csv)
# print(res)


def reader_for_excel(path):
    """Читает Excel-файл и возвращает список транзакций в формате, совместимом с JSON."""
    df = pd.read_excel(path)
    records = df.to_dict(orient="records")
    normalized = []
    for r in records:
        normalized.append(
            {
                "id": r.get("id"),
                "state": r.get("state"),
                "date": r.get("date"),
                "operationAmount": {
                    "amount": str(r.get("amount", "")),
                    "currency": {"name": r.get("currency_name", ""), "code": r.get("currency_code", "")},
                },
                "description": r.get("description", ""),
                "from": r.get("from", ""),
                "to": r.get("to", ""),
            }
        )
    return normalized


# result = reader_for_excel(path_of_excel)
# print(result)
