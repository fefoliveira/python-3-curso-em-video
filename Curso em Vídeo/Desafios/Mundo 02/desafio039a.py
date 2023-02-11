"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

— Se ele ainda vai se alistar ao serviço militar.
— Se é a hora de se alistar.
— Se já passou do tempo de alistamento.

O seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

ano = int(input('Digite o ano em que você nasceu: '))
print('Se você nasceu em {}, você fez/faz {} anos em 2022.'.format(ano, 2022 - ano))
if ano + 18 == 2022:
    print('Está na hora de você se alistar, você ja fez/vai fazer 18 anos esse ano.')
elif ano + 18 < 2022:
    print('Já passou da hora de você se alistar, você já fez 18 anos a {} anos.' .format(2022 - (ano + 18)))
elif ano + 18 > 2022:
    print('Ainda não chegou a hora de você se alistar, você faz 18 anos somente daqui {} anos.'.format(-(2022 - (ano + 18))))
