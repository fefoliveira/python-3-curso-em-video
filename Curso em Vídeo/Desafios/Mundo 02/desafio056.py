"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

— A média de idade do grupo.
— Qual é o nome do homem mais velho.
— Quantas mulheres têm menos de 20 anos."""

# Inicializar a var aqui em cima dá a opção de controlar ela mais tarde
média = 0  # Média de idade do grupo
mihomem = 0  # Maior idade do homem
nvelho = ''  # Nome do homem mais velho
mm20 = 0  # Mulher com menos de 20 anos
for c in range(1, 5):
    print('\033[33m{}ª PESSOA:\033[m'.format(c))
    nome = str(input('Nome: '.format(c))).strip().capitalize()
    idade = int(input('Idade: '.format(c)))
    sexo = str(input('Sexo biológico [M/F]: '.format(c))).strip().upper()
    média += idade / 4  # Soma o 0 da var no início do código e depois divide por 4
    if c == 1 and sexo == 'M':  # Se for o primeiro homem lido então o nome e a idade do mesmo vão ser as próprias var:
        mihomem = idade
        nvelho = nome
    if sexo == 'M' and idade > mihomem:  # Se houver um próximo homem e a idade dele for maior que a do anterior:
        mihomem = idade
        nvelho = nome
    if sexo == 'F' and idade < 20:
        mm20 += 1  # A cada mulher com menos de 20 anos, adiciona mais um no contador do mm20
print()
print('A média de idade do grupo é de {:.1f} anos.'.format(média))
print('O homem mais velho tem {} anos e o seu nome é {}.'.format(mihomem, nvelho))
print('Existem {} mulheres com menos de 20 anos no grupo.'.format(mm20))
