import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY_EXCHANGE_RATES")


def convert_transaction_amount(transaction):
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction["amount"]
    currency = transaction["currency"]
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=usd%2C%20eur&base=rub"
    payload = {}
    headers = API_KEY
    if currency == "RUB":
        return amount
    elif currency != "RUB":
        response = requests.request("GET", url, headers={"apikey": API_KEY}, data=payload)
        print(response.json())
        if response.status_code == 200:
            rate = response.json()["rates"][currency]
            amount = round(amount / rate, 2)
            return amount


@patch("requests.request")
def test_convert_transaction_amount(mock_requests):
    mock_response = {"rates": {"USD": 1.15}}
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.return_value = mock_response

    transaction = {"amount": 100, "currency": "USD"}
    assert convert_transaction_amount(transaction) == 86.96
    mock_requests.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/latest?symbols=usd%2C%20eur&base=rub",
        headers={"apikey": API_KEY},
        data={},
    )
