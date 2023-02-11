# Faça um alogritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento:
p = float(input('Qual o seu salário, em reais? '))
print('Apliquei um aumento de 15%! \nO novo valor do seu salário é de R${:.2f}.'.format(p+(p*0.15)))
