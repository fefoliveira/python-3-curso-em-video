"""Faça um programa que leia um número qualquer e mostre o seu fatorial (utilizando for).
Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input('Digite um número inteiro: '))
print('\033[33m{}!\033[m = '.format(n), end='')
c = n
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\033[33m{}\033[m'.format(f))
