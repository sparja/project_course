import json
from datetime import datetime


def open_file():
    with open('operations.json', 'r', encoding="utf-8") as operation:
        list_operations = json.load(operation)
        return list_operations


def main(sorted_transactions_date):
    for i in sorted_transactions_date[:5]:
        print(f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][:4]} {i['description']}")
        card_private(i['from'], i['to'])
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


def card_private(number_from, number_to):
    card_namber = number_from.split()[-1]
    private_number = card_namber[:6] + (len(card_namber[6:-4]) * '*') + card_namber[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    number_to_split = number_to.split()[-1]

    print(f'{number_from[:len(number_from) - len(card_namber)]}', end='')
    print(" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]), end=' --> ')
    print(f"{number_to[:len(number_to) - len(number_to_split)]}{len(number_to_split) * '*'}{number_to_split[:-5:-1]}")


# Функция для извлечения даты из транзакции
def get_transaction_date(transaction):
    if 'from' in transaction:
        return datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')
    return None


# Сортировка операций по дате в убывающем порядке
sorted_transactions = sorted(
    [transaction for transaction in open_file() if get_transaction_date(transaction) is not None],
    key=get_transaction_date, reverse=True)


if __name__ == '__main__':
    main(sorted_transactions)