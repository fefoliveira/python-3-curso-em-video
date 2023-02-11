# Escreva um programa que leia um valor em metros e o exiva convertido em centímetros e milímetros.
m = int(input('Digite uma medida em metros: '))
m1 = m*100
m2 = m*1000
print('Esta medida equivale a {} centímetros,'.format(m1), end='')
print(' bem como equivale a {} milímetros.'.format(m2))
