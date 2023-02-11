# Crie um programa qu leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('A cotação do dolar no dia de hoje (11/05/2022) é de US$1,00  = R$5,14.')
m = float(input('Quanto dinheiro você possui na sua carteira? '))
print('Na cotação de hoje, com seus R${:.2f} você pode comprar US${:.2f}.'.format(m, m/5.14))
