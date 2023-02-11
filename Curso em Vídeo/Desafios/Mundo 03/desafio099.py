"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros, com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def maior(*num):
    cont = maior = 0
    print('-' * 40, '\nAnalisando os valores:', end=' ')
    for c in num:
        print(f'{c}', end=' ')
        cont += 1
        if cont == 1:
            maior = c
        elif c > maior:
            maior = c
    print(f'\nO maior número informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()




