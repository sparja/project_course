import json
from datetime import datetime


def open_file():
    with open('operations.json', 'r', encoding="utf-8") as operation:
        list_operations = json.load(operation)
        return list_operations

def main(list_operations):
    count = 0
    for i in list_operations:
        count += 1
        if i['description'] == 'Открытие вклада':
            continue
        elif count > 5:
            break
        print(i)
        print(f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][:4]} {i['description']}")
        card_private(i['from'])


def card_private(number):
    card_namber = number.split()[-1]

    private_number = card_namber[:6] + (len(card_namber[6:-4]) * '*') + card_namber[-4:]

    chunks, chunk_size = len(private_number), len(private_number) // 4
    print(" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]))
    print(f'{number[:len(number) - len(card_namber)]}')


get_func(open_file())