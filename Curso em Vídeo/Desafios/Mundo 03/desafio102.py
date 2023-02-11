"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado "show", que será um valor lógico
(opcional) indicando se será mostrado ou nao na tela o processo de cálculo do fatorial."""


def fatorial(num, show=False):
    print(f'{num}! =', end=' ')
    for c in range(num, 0, -1):
        num *= c
        if show:
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
    print(num)


fatorial(5, True)
