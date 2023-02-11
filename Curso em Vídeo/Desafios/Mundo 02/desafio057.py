"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso eteja errado, peça a digitação novamente até ter um valor correto."""

s = ''
nome = str(input('Digite seu nome: ')).strip().capitalize()
sexo = str(input('Qual seu sexo biológico? [M/F]: ')).strip().upper()[0]  # Esse [0] pega só a primeira letra da str
while sexo not in 'MF':
    sexo = str(input('\033[31mErro!\033[m Digite seu sexo biológico novamente. [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    s = 'masculino'
if sexo == 'F':
    s = 'feminino'
print('Então seu nome é {} e você é do sexo biológico {}. '
      '\nPrazer em te conhecer, {}!'.format(nome, s, nome))
