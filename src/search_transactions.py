import os
import re
from collections import Counter

from src.utils import read_transactions_from_json

list_transactions = read_transactions_from_json(os.path.join("../data/operations.json"))


def return_list_dicts_with_transaction(list_dict: list, search_str: str) -> list:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    new_list = []
    for transaction in list_dict:
        if "description" in transaction and re.findall(search_str, transaction["description"]):
            new_list.append(transaction)
    return new_list


def sort_transactions(list_dict_trsn: list, categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_categories_transaction = []
    for transaction in list_dict_trsn:
        if "description" in transaction and transaction["description"] in categories:
            list_categories_transaction.append(transaction["description"])
    sort_transaction = Counter(list_categories_transaction)
    return dict(sort_transaction)


if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

print(sort_transactions(list_transactions, categories_operations))

input_user = input("Введите слово для поиска: ")
print(return_list_dicts_with_transaction(list_transactions, input_user))
