"""Elabore um programa que calcule o valor a ser pago por um produto, cosiderando o seu preço normal e condição de pagamento:

— À vista dinheiro/cheque: 10% de desconto
— À vista no cartão: 5% de desconto
— Em até 2x no cartão: preço normal
— 3x ou mais no cartão: 20% de juros"""

valor = float(input('Digite o valor do produto a ser pago: R$'))
pag = int(input('Digite a condição de pagamento: '
                '\n[ 1 ] para à vista dinheiro/cheque '
                '\n[ 2 ] para à vista no cartão '
                '\n[ 3 ] para em até 2x no cartão '
                '\n[ 4 ] para em 3x ou mais no cartão'
                '\nSua opção: '))
if pag == 1:
    print('Você recebeu um \033[32mdesconto de 10%\033[m! O valor total do seu produto ficou em \033[32mR${:.2f}\033[m.'.format(valor * 0.9))
elif pag == 2:
    print('Você recebeu um \033[32mdesconto de 5%\033[m! O valor total do seu produto ficou em \033[32mR${:.2f}\033[m.'.format(valor * 0.95))
elif pag == 3:
    print('Você não recebeu nenhum desconto. Sua compra ficou parcelada em 2x de \033[32mR${}\033[m sem juros e o valor total do seu produto ficou em \033[32mR${:.2f}\033[m.'.format(valor / 2, valor))
elif pag == 4:
    parc = int(input('Em quantas vezes no cartão? '))
    total = valor + (valor * 0.2)
    print('Você terá que pagar \033[31m20% de juros\033[m no total da compra. '
          '\nSua compra ficou parcelada em {}x de \033[32mR${:.2f}\033[m e o valor total do seu produto ficou em \033[32mR${:.2f}\033[m.'.format(parc, total / parc, total))
else:
    print('\033[31mERRO!\033[m Opção inválida, tente novamente.')
