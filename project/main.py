from project.func import card_private
from project.func import sort_data


def main(sorted_transactions_date):
    """Основная функция вывода данных"""
    for transaction in sorted_transactions_date[:5]:
        print(
            f"{transaction['date'][8:10]}.{transaction['date'][5:7]}.{transaction['date'][:4]} {transaction['description']}")
        card_private(transaction['from'], transaction['to'])
        print(f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    main(sort_data())
