"""Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA (em qualquer lugar) no nome."""

nome = str(input('Digite o seu nome completo: ')).strip().upper()
nome1 = 'SILVA' in nome
print('Seu nome completo possui o sobrenome SILVA? {}'.format(nome1))
