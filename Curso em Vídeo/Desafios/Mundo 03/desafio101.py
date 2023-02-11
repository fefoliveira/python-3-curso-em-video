"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicado se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições"""


def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    print(f'Com {idade} anos você', end=' ')
    if idade < 16:
        return '\033[31mnão pode votar\033[m.'
    elif 16 <= idade <= 17 or idade > 65:
        return '\033[34mtem direito ao voto opcional\033[m.'
    else:
        return '\033[32mé obrigado a votar\033[m.'


print(voto(2002))
