"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, t))
if t == 2:
    print('E por isso, este número \033[32mé primo\033[m.')
else:
    print('E por isso, este número \033[31mnão é primo\033[m.')
