"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] saber qual o maior
[4] novos números
[5] sair do programa
Seu progrma deverá realizar a operação solicitada em cada caso."""

from time import sleep
n1 = int(input('Digite o 1º valor inteiro: '))
n2 = int(input('Digite o 2º valor inteiro: '))
op = 0
while op != 5:
    op = int(input('\033[33mSelecione a operação:\033[m '
                   '\n[1] somar'
                   '\n[2] multiplicar'
                   '\n[3] saber qual o maior'
                   '\n[4] inserir novos números'
                   '\n[5] sair do programa'
                   '\nSua escolha: '))
    print()
    if op == 1:
        soma = n1 + n2
        print('\033[34mA soma entre os números digitados é {}.\033[m'.format(soma))
        print()
    elif op == 2:
        mult = n1 * n2
        print('\033[34mA multiplicação entre os números digitados é {}.\033[m'.format(mult))
        print()
    elif op == 3:
        if n1 > n2:
            print('\033[34mO maior dos números digitados é {}, e o menor {}.\033[m'.format(n1, n2))
            print()
        else:
            print('\033[34mO maior dos números digitados é {}, e o menor {}.\033[m'.format(n2, n1))
            print()
    elif op == 4:
        n1 = int(input('Digite novamente o 1º valor inteiro: '))
        n2 = int(input('Digite novamente o 2º valor inteiro: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('\033[31mErro!\033[m Tente novamente.')
        print()
    sleep(2)
print('\033[31mFim do programa.\033[m')
