def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    str_card_number = str(card_number)
    return f"({str_card_number[0:4]} {str_card_number[4:6]} **** ** {str_card_number[-4:]}"


def get_mask_account(account: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    str_account = str(account)
    return f"**{str_account[-4:]}"
