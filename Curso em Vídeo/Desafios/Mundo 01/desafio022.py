'''Crie um programa que leia o norme completo de uma pessoa e mostre:
-> O nome com todas as letras maísculas;
-> O nome com todas minúsculas;
-> Quantas letras ao todo (sem considerar espaços);
-> Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome inteiramente em maísculas: {}.'.format(nome.upper()))
print('Seu nome inteiramente em minúsculas: {}.'.format(nome.lower()))
print('Seu nome tem {} caractéres.'.format(len(nome)-nome.count(' ')))
nome1 = nome.split()
print('Seu primeiro nome tem {} caractéres.'.format(len(nome1[0])))
