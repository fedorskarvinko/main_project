from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция принимает на вход строку с информацией — тип карты/счета и номер карты/счета,
    возвращает исходную строку с замаскированным номером карты/счета.
    """
    parts = account_card.split(" ")
    if parts[0] == "Счет":
        return f"{parts[0]} **{parts[1][-4:]}"
    else:
        mask_card = get_mask_card_number(int(parts[-1]))
        del parts[-1]
        name_card = " ".join(parts)
        return f"{name_card} {mask_card} "


def get_data(data: str) -> str:
    """
    Функция преобразует дату из ГГГ-ММ-ДД в ДД-ММ-ГГГГ
    """
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"


print(mask_account_card("Visa Platinum 8990922113665229"))
