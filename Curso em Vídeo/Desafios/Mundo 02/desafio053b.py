f = str(input('Digite uma frase, sem acentos: ')).strip().upper()
p = f.split()
tj = ''.join(p)
inv = tj[::-1]
print('O inverso da frase "{}" é "{}".'.format(tj, inv))
if inv == tj:
    print('A frase digitada \033[32mé\033[m um palíndromo!')
else:
    print('A frase digitada \033[31mnão é\033[m um palíndromo.')
