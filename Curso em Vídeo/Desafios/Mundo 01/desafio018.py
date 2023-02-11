'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
a = float(input('Digite um ângulo em graus: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O seno, cosseno e tangente desse ângulo equivalem, respectivamente,1 a {:.2f}, {:.2f} e {:.2f}.'.format(sin, cos, tg))
