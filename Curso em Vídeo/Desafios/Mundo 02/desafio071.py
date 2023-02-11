"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS.: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50."""

# Resolução do Guanabara, não entendi muito bem.
v = int(input('Digite o valor que você quer sacar: R$'))
tot = v
ced = 50
totced = 0
while True:
    if tot >= ced:  # Se o total de cédulas for maior que 50:
        tot -= ced  # Tira 50 até o total não ser maior ou igual a 50
        totced += 1  # Conta o tanto de cédulas usadas
    else:  # Se o tot não for maior ou igual a 50:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20   # Reduz o valor da cédula para descontar um novo valor até chegar a zero
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:  # Se todo o valor tiver sido descontado em cédulas:
            break
