from project.func import card_private_from, card_private_to, sort_data



def main():
    """Основная функция вывода данных"""
    for transaction in sort_data()[:5]:
        print(
            f"{transaction['date'][8:10]}.{transaction['date'][5:7]}.{transaction['date'][:4]} {transaction['description']}")
        print(card_private_from(transaction), end=" --> ")
        print(card_private_to(transaction))
        print(f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
        print()

if __name__ == '__main__':
    main()
