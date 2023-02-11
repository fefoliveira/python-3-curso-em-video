"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

— 1 para binário
— 2 para octal
— 3 para hexadecimal"""

n = int(input('Digite um número: '))
bin = bin(n)
oct = oct(n)
hex = hex(n)
base = int(input('Digite a base de conversão desejada: '
                 '\n[ 1 ] para binário '
                 '\n[ 2 ] para octal '
                 '\n[ 3 ] para hexadecimal '
                 '\nSua opção: '))
if base == 1:
    print('{} convertido em uma base \033[33mBINÁRIA\033[m corresponde a \033[34m{}\033[m.'.format(n, bin[2:]))
elif base == 2:
    print('{} convertido em uma base \033[33mOCTAL\033[m corresponde a \033[34m{}\033[m.'.format(n, oct[2:]))
elif base == 3:
    print('{} convertido em uma base \033[33mHEXADECIMAL\033[m corresponde a \033[34m{}\033[m.'.format(n, hex[2:]))
