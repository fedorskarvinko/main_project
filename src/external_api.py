import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY_EXCHANGE_RATES")


def convert_transaction_amount(transaction):
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction["amount"]
    currency = transaction["currency"]
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {}
    # headers = API_KEY
    if currency == "RUB":
        return float(amount)
    elif currency != "RUB":
        response = requests.request("GET", url, headers={"apikey": API_KEY}, data=payload)
        print(response.json())
        if response.status_code == 200:
            rate = response.json()["rates"][currency]
            amount = round(amount / rate, 2)
            return float(amount)
