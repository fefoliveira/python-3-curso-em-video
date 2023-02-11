"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

— O primeiro valor é maior
— O segundo valor é maior
— Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print('O número \033[33m{}\033[m é maior.'.format(n1))
elif n1 < n2:
    print('O número \033[33m{}\033[m é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são \033[33miguais\033[m.')
