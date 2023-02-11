"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

from math import fabs
n1 = float(input('Digite comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra: '))
n3 = float(input('Agora o de mais uma: '))
if n1 > fabs(n2 - n3):
    if n1 < (n2 + n3):
        print('É possível formar um triângulo com essas retas.')
    else:
        if n2 > fabs(n1 - n3):
            if n2 < (n1 + n3):
                print('É possível formar um triângulo com essas retas.')
            else:
                if n3 > fabs(n1 - n2):
                    if n3 < (n1 + n2):
                        print('É possível formar um triângulo com essas retas.')
                    else:
                        print('É possível formar um triângulo com essas retas.')
                else:
                    print('É possível formar um triângulo com essas retas.')
        else:
            print('Não é possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
