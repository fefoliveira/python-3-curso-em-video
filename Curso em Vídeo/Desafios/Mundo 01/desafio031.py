"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas."""

d = float(input('Digite a distância a percorrer em sua viagem, em Km: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
# p = d * 0.50 if d <= 200 else d * 0.45
print('O valor da sua viagem ficará em R${:.2f}.'.format(p))
