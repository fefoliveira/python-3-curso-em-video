r = 'S'
while r == 'S':  # Enquanto a resposta não for sim, repete o laço
    n = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
print('\033[31mFim.\033[m')
