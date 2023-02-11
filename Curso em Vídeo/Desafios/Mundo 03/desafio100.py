"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior."""


from random import randint


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Foram sorteados os números:', end=' ')
    for c in numeros:
        print(f'{c}', end=' ')


def somaPar():
    pares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += num
    print(f'\nA soma dos valores pares sorteados equivale a {pares}.')


numeros = list()
sorteia()
somaPar()
