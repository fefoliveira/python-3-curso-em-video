"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas;
    B) A média de idade do grupo;
    C) Uma lista com todas as mulheres;
    D) Uma lista com todas as pessoas com idade acima da média."""

lista = list()
pessoas = dict()
mulheres = list()
velhos = list()
cont = 0
while True:
    cont += 1
    pessoas['nome'] = str(input(f'Digite o nome da {cont}ª pessoa: ')).capitalize()
    pessoas['sexo'] = str(input(f'Digite o sexo biológico da {cont}ª pessoa [M/F]: ')).upper()
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input(f'Inválido! Digite novamente o sexo biológico da {cont}ª pessoa [Digite apenas M/F]: ')).upper()
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input(f'Digite a idade da {cont}ª pessoa: '))
    while pessoas['idade'] < 0:
        pessoas['idade'] = int(input(f'Inválido! Digite novamente a idade da {cont}ª pessoa: '))
    lista.append(pessoas.copy())
    continua = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).upper()
    while continua not in 'SN':
        continua = str(input('Inválido! Deseja cadastrar mais uma pessoa? [Digite apenas S/N]: ')).upper()
    print()
    if continua == 'N':
        break
soma = 0
for k in range(0, len(lista)):
    soma += lista[k]['idade']
media = soma/len(lista)
for k in range(0, len(lista)):
    if lista[k]['idade'] > media:
        velhos.append(lista[k]['nome'])
print(f'Foram cadastradas um total de {len(lista)} pessoas.')
print(f'A média de idade do grupo de pessoas é de {media} anos.')
if len(mulheres) > 0:
    print(f'As mulheres do grupo são: {mulheres}')
print(f'As pessoas do grupo com idade acima da média são: {velhos}')
