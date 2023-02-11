from datetime import date
ano = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # != significa ≠
    print('O ano de {} ano é bissexto!'.format(ano))
else:
    print('O ano de {} ano não é bissexto.'.format(ano))
