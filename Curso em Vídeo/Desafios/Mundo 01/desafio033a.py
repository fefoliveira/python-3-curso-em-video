"""Faça um programa que leia três números e mostre qual é o maior e qual o menor."""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Agora mais um: '))
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n1, n3))
        else:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n1, n2))
    else:
        if n3 > n2:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n3, n1))
        else:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n3, n2))
else:
    if n2 > n3:
        if n3 > n1:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n2, n1))
        else:
            print('Entre esses três números, o maior é {} e o menor {}.'.format(n2, n3))
    else:
        print('Entre esses três números, o maior é {} e o menor {}.'.format(n3, n1))
