"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

— Abaixo de 18.5: Abaixo do peso
— Entre 18.5 e 25: Peso ideal
— 25 até 30: Sobrepeso
— 30 até 40: Obesidade
— Acima de 40: Obesidade mórbida"""

peso = float(input('Digite seu peso, em Kg: '))
alt = float(input('Digite sua altura, em m: '))
imc = peso / (alt ** 2)
if imc <= 18.5:
    print('O seu IMC corresponde a {:.1f} e você se enquadra como \033[31mABAIXO DO PESO\033[m.'.format(imc))
elif 18.5 <= imc <= 25:
    print('O seu IMC corresponde a {:.1f} e você se está no \033[32mPESO IDEAL\033[m.'.format(imc))
elif 25 <= imc <= 30:
    print('O seu IMC corresponde a {:.1f} e você se encontra em \033[33mSOBREPESO\033[m .'.format(imc))
elif 30 <= imc <= 40:
    print('O seu IMC corresponde a {:.1f} e você está \033[31mOBESO\033[m.'.format(imc))
elif imc > 40:
    print('O seu IMC corresponde a {:.1f} e você se encontra em \033[31mOBESIDADE MÓRBIDA\033[m.'.format(imc))
