"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensgem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

v = float(input('Digite a velocidade do carro, em Km/h: '))
if v > 80.0:
    m = float((v - 80) * 7)
    print('Você foi multado! Sua multa será cobrada no valor de R${:.2f}.'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
