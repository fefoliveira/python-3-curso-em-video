"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida;

— Média abaixo de 5.0:
REPROVADO
— Média entre 5.0 e 6.9:
RECUPERAÇÃO
— Média 7.0 ou superior:
APROVADO"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2) / 2
if med < 5.0:
    print('Você obteve uma média {:.1f}, infelizmente não foi satisfatória, você foi \033[31mREPROVADO\033[m.'.format(med))
elif 5.0 <= med <= 6.9:
    print('Você obteve uma média {:.1f}, infelizmente não foi o suficiente e você terá que realizar uma \033[33mRECUPERAÇÃO\033[m.'.format(med))
elif med >= 7.0:
    print('Você obteve uma média {:.1f}, foi completamente satisfatória, você está \033[32mAPROVADO\033[m.'.format(med))
