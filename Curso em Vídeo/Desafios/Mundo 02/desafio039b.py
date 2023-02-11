from datetime import date
atual = date.today().year
ano = int(input('Digite o ano em que você nasceu: '))
idade = atual - ano
print('Se você nasceu em {}, você fez/faz {} anos em 2022.'.format(ano, 2022 - ano))
if idade == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m!')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    alist = atual - saldo
    print('Seu alistamento foi em {}.'.format(alist))
elif idade < 18:
    saldo = idade - 18
    print('Ainda faltam {} anos para seu alistamento.'.format(-(saldo)))
    alist = atual + -saldo
    print('Seu alistamento será em {}.'.format(alist))
