from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator():
    number_generator = card_number_generator(1, 5)
    assert next(number_generator) == "0000 0000 0000 0001"
    assert next(number_generator) == "0000 0000 0000 0002"
    assert next(number_generator) == "0000 0000 0000 0003"
    assert next(number_generator) == "0000 0000 0000 0004"
