import json
from datetime import datetime


def open_file():
    """
    Функция открывающая файл
    :return: список json
    """
    with open('operations.json', 'r', encoding="utf-8") as operation:
        list_operations = json.load(operation)
        return list_operations


def card_private_from(sorted_transactions):
    """
    Функция преобразования номера счета
    :param sorted_transactions: Сортированный список
    :return: Вернет перобразованный номер
    """
    number_from = sorted_transactions['from']
    number_from_split = number_from.split(" ")[-1]
    if "Счет" in sorted_transactions['from']:
        return f"{number_from[:len(number_from) - len(number_from_split)] + '**' + number_from_split[-4:]}"

    return number_from[:len(number_from) - len(number_from_split)] + number_from_split[:4] \
        + " " + number_from_split[4:6] + '*' * 2 + " " + '****' + " " + number_from_split[-4:]


def card_private_to(sorted_transactions):
    """
    Функция преобразования номера счета
    :param sorted_transactions: Сортированный список
    :return: Вернет перобразованный номер
    """
    number_to = sorted_transactions['to']
    number_to_split = number_to.split(" ")[-1]
    if "Счет" in sorted_transactions['to']:
        return f"{number_to[:len(number_to) - len(number_to_split)] + '**' + number_to_split[-4:]}"
    return number_to[:len(number_to) - len(number_to_split)] + number_to_split[:4] \
        + " " + number_to_split[4:6] + '*' * 2 + " " + '****' + " " + number_to_split[-4:]


def get_transaction_date(transaction):
    """
    Функция для извлечения даты из транзакции
    :param transaction:
    :return:
    """
    if 'from' in transaction and transaction['state'] == 'EXECUTED':
        return datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')
    return None


def sort_data():
    """
    Сортировка операций по дате в убывающем порядке
    :return:
    """
    sorted_transactions = sorted(
        [transaction for transaction in open_file() if get_transaction_date(transaction) is not None],
        key=get_transaction_date, reverse=True)

    return sorted_transactions





