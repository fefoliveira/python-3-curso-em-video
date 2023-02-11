"""Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o condeúdo da estrutura na tela."""

dic = dict()
dic['nome'] = str(input('Nome: ')).capitalize()
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] >= 6:
    dic['sit'] = 'Aprovado(a)'
else:
    dic['sit'] = 'Reprovado(a)'
print(f'\nSituação de {dic["nome"]} = {dic["sit"]}')
