import json
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"..\\logs\\utils.log", mode="w", encoding='utf-8')
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_transactions_from_json(file_path):
    """
    Функцию, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    logger.info(f'Принимаем путь до файла')
    try:
        logger.info(f'Открываем файл по заданному пути')
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f'Произошла ошибка')
        return []
