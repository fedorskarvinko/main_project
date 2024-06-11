def mask_account_card(account_card: str) -> str:
    """
    Функция принимает на вход строку с информацией — тип карты/счета и номер карты/счета,
    возвращает исходную строку с замаскированным номером карты/счета.
    """
    parts = account_card.split()
    if parts[0] in ["Visa", "Maestro"]:
        return f"{parts[0]} {parts[1]} {parts[2]} {parts[3][:2]}** **** {parts[5]}"
    elif parts[0] == "Счет":
        return f"{parts[0]} **{parts[1][-4:]}"


#def get_data(data: str) -> str:
