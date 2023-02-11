'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127
     O número 6.127 tem a parte inteira 6.'''
import math
n = float(input('Digite um número: '))
parte = math.trunc(n)
print('O número {} tem como parte inteira {}.'.format(n , parte))
