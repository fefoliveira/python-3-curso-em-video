"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime
pessoa = dict()
pessoa['nome'] = (str(input('Digite o nome: '))).capitalize()
ano = (int(input('Digite o ano de nascimento: ')))
pessoa['idade'] = datetime.today().year - ano
pessoa['ctps'] = (int(input('Digite a carteira de trabalho: ')))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = (int(input('Digite o ano de contratação: ')))
    pessoa['salario'] = (int(input('Digite o salário: R$')))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (datetime.today().year - pessoa['contratacao']))
print()
for k, v in pessoa.items():
    print(f'{k} = {v}')
