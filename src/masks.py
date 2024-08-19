import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "masks.log"), mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    logger.info("Принимаем номер карты")
    str_card_number = str(card_number)
    return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    logger.info("Принимаем номер счета карты")
    str_account = str(account)
    return f"**{str_account[-4:]}"
