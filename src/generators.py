def filter_by_currency(transactions, currency):
    """
    Функция, которая принимает список словарей с банковскими операциями
    (или объект-генератор, который выдает по одной банковской операции)
     и возвращает итератор, который выдает по очереди операции,
     в которых указана заданная валюта.
     """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
      Генератор, который принимает список словарей с банковскими операциями
      и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт, который генерирует номера карт в формате
    XXXX XXXX XXXX XXXX , где X — цифра.
    """
    for i in range(start, end + 1):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
