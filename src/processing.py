def filter_by_state(dict_list: list, key_state: str = "EXECUTED") -> list:
    """
    Функция, которая принимает на вход список словарей и значение для ключа state
     и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение.
    """
    filt_list = []
    for i in range(len(dict_list)):
        if dict_list[i]["state"] == key_state:
            filt_list.append(dict_list[i])
    return filt_list


def sort_by_date(list_with_date: list, order: bool = True) -> list:
    """
    Функция, которая принимает на вход список словарей и возвращает новый список,
     в котором исходные словари отсортированы по убыванию даты.
    """
    sort_list = sorted(list_with_date, key=lambda list_: list_.get("date"), reverse=order)
    return sort_list
