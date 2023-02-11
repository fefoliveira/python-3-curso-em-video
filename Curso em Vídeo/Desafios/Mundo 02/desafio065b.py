# Resolução correta do Guanabara:
# Está cheia de erros, um exemplo é quando o dedo escapa e aperta alguma letra que difere de S ou N.
# Outro erro é quando é digitado um espaço, ou nada ao invés de uma letra, e tem mais alguns outros.
r = 'S'
soma = c = media = maior = menor = 0
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = str(input('Você gostaria de continuar a digitar valores? [S/N]: ')).strip().upper()[0]
media = soma / c
print('Você digitou {} valores.'
      '\nA média entre eles é de {:.2f}, o maior valor lido foi {} e o menor {}.'.format(c, media, maior, menor))
