"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. """

valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você quer pagar o empréstimo: '))
prest = valor / (anos * 12)
print('A prestação de uma casa de R${:.2f} a ser paga em {} anos será de R${:.2f}.'.format(valor, anos, prest))
if prest <= sal*0.30:
    print('Parabéns! O seu empréstimo foi \033[32mAPROVADO\033[m!')
else:
    print('Infelizmente o seu empréstimo foi \033[31mNEGADO\033[m.')
