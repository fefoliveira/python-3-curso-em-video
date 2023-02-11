"""Reescreva a função leiaInt() que fizemos no desafio104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(a):
    while True:
        try:
            num = int(input(a))
        except KeyboardInterrupt:
            print('\033[31m\nERRO! O usuário preferiu não digitar esse número.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite somente números inteiros.\033[m')
        else:
            return num


def leiaFloat(a):
    while True:
        try:
            num = float(input(a))
        except KeyboardInterrupt:
            print('\033[31mERRO! Nada foi digitado.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite somente números reais.\033[m')
        else:
            return num


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'\033[32m\nO valor inteiro digitado foi {i} e o real foi {r}.\033[m')
