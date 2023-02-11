# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto, em reais? '))
print('Apliquei um desconto de 5%! \nO novo preço do produto é de R${:.2f}.'.format(p-(p*0.05)))
