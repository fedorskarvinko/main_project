import json


def read_transactions_from_json(file_path):
    """
    Функцию, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
