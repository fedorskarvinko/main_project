import os
from src.file_reader import read_transactions_csv_file, read_transactions_excel_file
from src.processing import filter_by_state, sort_by_date
from src.utils import read_transactions_from_json
from src.widget import get_data
from src.search_transactions import return_list_dicts_with_transaction
from src.masks import get_mask_card_number


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функции между собой."""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_file_choice = input().strip()
        if user_file_choice == "1":
            print("Выбран JSON-файл.")
            list_transactions = read_transactions_from_json(os.path.join("../main_project/data/operations.json"))
            break
        elif user_file_choice == "2":
            print("Выбран CSV-файл.")
            list_transactions = read_transactions_csv_file(os.path.join("../main_project/data/transactions.csv"))
            break
        elif user_file_choice == "3":
            print("Выбран XLSX-файл.")
            list_transactions = read_transactions_excel_file(os.path.join("../main_project/data/transactions_excel.xlsx"))
            break
        else:
            print("Некорректный выбор. Попробуй еще раз.")
            continue

    list_transactions: dict[str, str | bool] = {}
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            list_transactions["status"] = status
            print(f"Операции отфильтрованы по статусу {status}")
            break
        else:
            print("Некорректный выбор. Попробуй еще раз.")
            continue
    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sorting_order = input(
                    """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
                ).lower()
                if sorting_order == "по возрастанию":
                    list_transactions["date"] = False
                    break
                elif sorting_order == "по убыванию":
                    list_transactions["date"] = True
                    break
                else:
                    print("Некорректно выбрал. Пробуй еще раз.")
                    continue
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректно выбрал. Пробуй еще раз.")
            continue
    while True:
        sort_code = str(input("Выводить только рублевые транзакции? Да/Нет\n")).lower()
        if sort_code == "да":
            list_transactions["currency"] = "RUB"
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректно выбрал. Пробуй еще раз.")
            continue
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            list_transactions["description"] = search
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректно выбрал. Пробуй еще раз.")
            continue

    transactions = list_transactions
    for filter_type, filter_value in list_transactions.items():
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                txn
                for txn in transactions
                if txn.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
            ]
        elif filter_type == "description":
            transactions = return_list_dicts_with_transaction(transactions, filter_value)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = get_mask_card_number(transaction.get("from"))

        to_ = get_mask_card_number(transaction.get("to"))
        date = get_data(transaction.get("date"))

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
