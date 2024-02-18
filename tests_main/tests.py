from datetime import datetime

import pytest
from project.func import get_transaction_date, card_private_from, card_private_to


def test_card_private_from():
    """
    Тест для номера счета !="Счет"
    :return:
    """
    sorted_transactions = {'from': 'Maestro 1596837868705199'}
    result = card_private_from(sorted_transactions)
    assert result == 'Maestro 1596 83** **** 5199'

def test_card_private_from_():
    """
    Тест для номера счета 'Счет'
    :return:
    """
    sorted_transactions = {'from': 'Счет 1234567891234567'}
    result = card_private_from(sorted_transactions)
    assert result == 'Счет **4567'

def test_card_private_to():
    """
    Тест для номера счета !="Счет"
    :return:
    """
    sorted_transactions = {'to': 'Maestro 1596837868705199'}
    result = card_private_to(sorted_transactions)
    assert result == 'Maestro 1596 83** **** 5199'

def test_card_private_to_():
    """
    Тест для номера счета 'Счет'
    :return:
    """
    sorted_transactions = {'to': 'Счет 1234567891234567'}
    result = card_private_to(sorted_transactions)
    assert result == 'Счет **4567'

def test_get_transaction_date():
    """
     Проверка извлечения даты
    :return:
    """
    transaction = {"date": "2022-09-15T10:30:00.123456", "from": "Card 1234", "state": "EXECUTED"}
    assert get_transaction_date(transaction) == datetime(2022, 9, 15, 10, 30, 0, 123456)


def test_get_transaction_date_invalid_state():
    """
    Проверка, что дата возвращается None для транзакции с неверным статусом
    :return:
    """
    transaction = {"date": "2022-09-15T10:30:00.123456", "from": "Card 1234", "state": "CANCELLED"}
    assert get_transaction_date(transaction) is None


if __name__ == "__main__":
    pytest.main()
