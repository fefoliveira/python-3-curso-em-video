# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quatidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Kms você percorreu? '))
d = float(input('Por quantos dias você alugou o carro? '))
print('Você deverá pagar R${} pela locação do carro.'.format((d*60)+(km*0.15)))
