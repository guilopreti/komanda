from .management import add_item_to_tab, calculate_tab

import os


TABLE_TAB = []


def initial_screen():
    if len(TABLE_TAB) == 0:
        os.system("clear")

    while True:

        print("1. Adicionar item a comanda")
        print("2. Fechar comanda")
        resposta = input("Digite o que deseja fazer: ")

        if resposta == "1":
            add_item_screen()
        elif resposta == "2":
            check_out_screen()
        else:
            os.system("clear")
            print("Digite uma opção válida (1 ou 2)")


def add_item_screen():
    os.system("clear")

    while True:

        item_id = input("Digite o id do item: ")
        amount = input("Digite a quantidade desejada: ")

        add_product = add_item_to_tab(TABLE_TAB, int(item_id), int(amount))

        if not add_product:
            os.system("clear")
            print(f'{item_id} não é um id de item valido')
        else:
            break

    os.system("clear")
    amount = TABLE_TAB[-1]["amount"]
    name = TABLE_TAB[-1]["name"]
    print(f"{amount} {name} adicionado(s) a comanda!")
    initial_screen()


def check_out_screen():
    while True:
        os.system("clear")

        for index, item in enumerate(TABLE_TAB):
            num = index + 1
            amount = item["amount"]
            name = item["name"]
            price = item["price"]
            print(
                f'Item {num}: {amount} {name} - R${round(price * amount, 2)}'
                )

        print("-" * 100)

        print(f'Total: R${round(calculate_tab(TABLE_TAB), 2)}')

        resposta = input("Digite F para finalizar o sistema\n")

        if resposta.upper() == "F":
            exit()
