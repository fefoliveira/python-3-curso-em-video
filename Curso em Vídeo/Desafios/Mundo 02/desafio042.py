"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

— Equilátero: todos os lados iguais
— Isósceles: dois lados iguais
— Escaleno: todos os lados diferentes"""

from math import fabs
n1 = float(input('Digite comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra: '))
n3 = float(input('Agora o de mais uma: '))
if fabs(n2 - n3) < n1 < (n2 + n3) and n1 == n2 == n3:
    print('É possível formar um triângulo EQUILÁTERO com essas retas.')
elif fabs(n2 - n3) < n1 < (n2 + n3) and n1 == n2 or n1 == n3 or n2 == n3:
    print('É possível formar um triângulo ISÓSCELES com essas retas.')
elif fabs(n2 - n3) < n1 < (n2 + n3) and n1 != n2 != n3:
    print('É possível formar um triângulo ESCALENO com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
