import csv

import pandas as pd


def read_transactions_csv_file():
    """Функция, которая считывает финансовые операции из CSV файлов"""
    with open("C:/Users/fedor/Downloads/transactions.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        result = []
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)

    return result


def read_transactions_excel_file():
    """Функция, которая считывает финансовые операции из EXEL файлов """
    df = pd.read_excel('C:/Users/fedor/Downloads/transactions_excel.xlsx')  # читаем из экселя в DataFrame
    result = []
    rows_count = len(df)
    for i in range(0, rows_count):
        row_dict = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": df.at[i, "from"],
            "to": df.at[i, "to"],
        }
        result.append(row_dict)
    return result

