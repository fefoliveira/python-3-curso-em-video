"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n = int(input('Digite um número: '))
n1 = n % 2
if n1 > 0:
    print('O número {} é IMPAR!'.format(n))
else:
    print('Esse número é PAR!')
