"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

— Até 9 anos: MIRIM
— Até 14 anos: INFANTIL
— Até 19 anos: JUNIOR
— Até 20 anos: SÊNIOR
— Acima: MASTER"""

from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = ano - nasc
if idade <= 9:
    print('Você pertence a categoria MIRIM, até 9 anos.')
elif 9 < idade <= 14:
    print('Você pertence a categoria INFANTIL, até 14 anos.')
elif 14 < idade <= 19:
    print('Você pertence a categoria JUNIOR, até 19 anos.')
elif 19 < idade <= 20:
    print('Você pertence a categoria SÊNIOR, até 20 anos.')
elif idade > 20:
    print('Você pertence a categoria MASTER, acima de 20 anos.')
