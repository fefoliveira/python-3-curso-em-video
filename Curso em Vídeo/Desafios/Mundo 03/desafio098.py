"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo,
e realiza a contagem. Seu programa tem que realizar três contagens através da função criada:
    a) De 1 até 10, de 1 em 1;
    b) De 10 até 0, de 2 em 2;
    c) Uma contagem personalizada."""

from time import sleep


def contador(i, f, p):
    print('-' * 40, f'\nContagem de {i} até {f} de {p} em {p}:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.3)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.3)
    print('\033[31mFIM!\033[m')
    sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40, '\nAgora é a sua vez de personalizar a contagem:')
contador(int(input('De: ')), int(input('Até: ')), int(input('De quanto em quanto? ')))
