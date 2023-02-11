"""Escreva o programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

s = float(input('Digite o seu salário: R$'))
if s > 1250:
    print('Você recebeu um aumento! Seu novo salário é de R${}.'.format(s + (s * 0.10)))
else:
    print('Você recebeu um aumento! Seu novo salário é de R${}.'.format(s + (s * 0.15)))
