"""Melhore o desafio061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos."""

print('\033[33mVeja os 10 termos de uma PA:\033[m')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r  # Fórmula do enézimo termo de uma PA
t = p  # Termo, que começa como o primeiro termo
c = 1  # Contador
tot = 0  # Total de termos
tt = 10  # Termos a mais solicitados
while tt != 0:
    tot += tt  # Faz com que o primeiro total de termos mostrados seja 10
    while c <= tot:
        print('\033[34m{}\033[m'.format(t), end='')
        print('\033[34m -> \033[m' if c != tot else '...', end='')
        t += r
        c += 1
    tt = int(input('\n\033[33mVocê gostaria de mostrar mais alguns termos?\033[m'
                   '\nSe sim, digite a quantia, se não, digite 0: '))
print('Você vizualizou {} termos, \033[31mprogressão finalizada\033[m.'.format(tot))
