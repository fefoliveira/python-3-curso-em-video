"""Faça um programa que leia um número qualquer e mostre o seu fatorial (utilizando while).
Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

# from math import factorial
# n = int(input('Digite um número inteiro: '))
# f = factorial(n)
# print('{}! = {}'.format(n, f))

n = int(input('Digite um número inteiro: '))
print('\033[33m{}!\033[m = '.format(n), end='')
c = n  # Para fatorial, o contador começa com o proprio n
f = 1  # O fator nulo de uma multiplicação é 1, diferente do de soma e subtração que é 0
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\033[33m{}\033[m'.format(f))