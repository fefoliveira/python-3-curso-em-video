"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente."""

notas = list()
alunos = list()
aux = list()
cont = 0
while True:
    cont += 1
    nome = str(input(f'Digite o nome do {cont}º aluno: '))
    nome = nome.capitalize()
    aux.append(nome[:])

    n1 = float(input(f'Digite o 1ª nota do {cont}º aluno: '))
    while n1 > 10 or n1 < 0:
        n1 = float(input(f'Inválido! Digite o 1ª nota do {cont}º aluno, entre 0 e 10: '))
    n2 = float(input(f'Digite o 2ª nota do {cont}º aluno: '))
    while n2 > 10 or n2 < 0:
        n2 = float(input(f'Inválido! Digite o 2ª nota do {cont}º aluno, entre 0 e 10: '))
    media = (n1 + n2) / 2
    aux.append(media)
    notas.append(n1)
    notas.append(n2)
    aux.append(notas[:])

    alunos.append(aux[:])
    notas.clear()
    aux.clear()
    continua = str(input('Deseja cadastrar mais alunos? [S/N]: '))
    while continua not in 'SsNn':
        continua = str(input('Inválido! Deseja cadastrar mais alunos? [S/N]: '))
    if continua in 'Nn':
        break

print(f'\nNo.  NOME          MÉDIA'
      f'\n-------------------------')
for c in range(0, len(alunos)):
    print(f'{c+1}    {alunos[c][0]}', end='')
    for i in range(0, 16-len(alunos[c][0])):
        print(' ', end='')
    print(f'{alunos[c][1]}')

while True:
    num = int(input('\nDeseja mostrar as notas individuais de qual aluno? (0 para interromper): '))
    while num < 0 or num > len(alunos):
        num = int(input('Inválido! Este número não consta na chamada, digite novamente. (0 para interromper): '))
    if num == 0:
        break
    else:
        print(f'As notas de {alunos[num-1][0]} são: {alunos[num-1][2]}')
