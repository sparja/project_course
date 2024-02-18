from datetime import datetime

import pytest
from project.func import open_file, get_transaction_date, sort_data





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
