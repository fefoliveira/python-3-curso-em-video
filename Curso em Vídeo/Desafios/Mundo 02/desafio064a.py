"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

c = 0
n = int(input('Digite um número inteiro (999 para parar): '))
s = n
if n != 999:
    c = 1
while n != 999:
    n = int(input('Digite outro número inteiro (999 para parar): '))
    c += 1
    s += n
if c == 2 and s >= 999:
    print('\033[33mFoi digitado somente o número {}.\033[m'.format(s - 999))
elif c == 0:
    print('\033[33mNenhum número foi digitado.\033[m')
elif c not in [0, 1, 2]:
    print('\033[33mForam digitados {} números e a soma entre eles equivale a {}.\033[m'.format(c - 1, s - 999))
print('\033[31mFim do programa.\033[m')
