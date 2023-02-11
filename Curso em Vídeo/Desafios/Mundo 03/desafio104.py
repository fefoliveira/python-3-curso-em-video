"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceiutar apenas um valor numérico."""


def leiaInt(a):
    while True:
        num = str(input(a))
        if not num.isnumeric():
            print('\033[31mERRO! Digite um número inteiro: \033[m')
        else:
            break
    return num


print(f'\033[32mO número digitado foi {leiaInt("Digite um número inteiro: ")}.\033[m')
