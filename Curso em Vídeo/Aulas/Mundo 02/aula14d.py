n = 1
# par = 0
# impar = 0
par = impar = 0
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n != 0:  # Só se o número diferir de zero vai seguir a lógica, porque zero não é par nem impar, é nulo.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
