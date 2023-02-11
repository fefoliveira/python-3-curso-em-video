# Código do Guanabara
n = c = soma = 0
n = int(input('Digite um número inteiro (999 para parar): '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número inteiro (999 para parar): '))
print('Foram digitados {} números e a soma entre eles equivale a {}.'.format(c, soma))
# Não foi preciso usar a gambirra do ".format(c - 1, s - 999)" pois ao colocar outro n no fim do while, o 999 não vai contabilizar nem para a soma nem para o c
