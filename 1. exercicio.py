"""
Dada uma lista de palavras, escreva um programa 
que receba uma lista de frutas e mostre:
- a lista original
- a lista ordenada
- a lista na ordem inversa
que inverta a ordem dos elementos da lista.
"""

import os

os.system("cls || clear")

def menu():
    print("="*40)
    print(f"{'1- Digite uma fruta':^40}")
    print(f"{'2- Digite visualizar lista original':^40}")
    print(f"{'3- Digite visualizar lista ordenada':^40}")
    print(f"{'4- Digite visualizar lista inversa':^40}")
    print(f"{'5- Sair':^40}")
    print("="*40)

def ordernando():
    lista_ordenada = sorted(lista_fruta)
    print("lista ordenada:")
    return lista_ordenada

def inversa():
    lista_inversa = sorted(lista_fruta, reverse=True)
    print("lista inversa:")
    return lista_inversa

lista_fruta = []


while True:
    menu()
    opcao = input("Digite uma opção: ")
    os.system("cls || clear")
    match opcao:
        case "1":
            fruta = input("Digite uma fruta: ")
            lista_fruta.append(fruta)
        case "2":
            print("lista original:")
            print(lista_fruta)
        case "3":
            ordernando()
        case "4":
            inversa()
        case "5":
            break
        case _:
            print("Opção invalida")
            continue


            

