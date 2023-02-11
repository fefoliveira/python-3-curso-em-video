'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# hip = (co**2+ca**2)**(1/2))
# hip = math.sqrt((co**2)+(ca**2))
hip = math.hypot(co, ca)
print('A hipotenusa desse triângulo equivale a {:.2f}.'.format(hip))
