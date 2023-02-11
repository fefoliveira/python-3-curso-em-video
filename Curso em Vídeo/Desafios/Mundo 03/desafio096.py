"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""

def area(a, b):
    print(f'\nA área do terreno é igual a {a * b:.2f}m²')


area(float(input('Digite o comprimento do terreno: ')), float(input('Digite a largura do terreno: ')))
