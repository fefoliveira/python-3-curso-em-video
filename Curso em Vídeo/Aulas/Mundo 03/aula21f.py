def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('O número digitado é par.')
else:
    print('O número digitado é impar.')
