galera = list()
aux = list()
tot_maior = tot_menor = 0
for c in range(0, 5):
    nome = str(input(f'{c + 1}º nome: '))
    aux.append(nome.capitalize())
    aux.append(int(input(f'{c + 1}ª idade: ')))
    print()
    galera.append(aux[:])
    aux.clear()
for pessoa in galera:
    if pessoa[1] >= 18:
        tot_maior += 1
        print(f'{pessoa[0]} é maior de idade.')
    else:
        tot_menor += 1
        print(f'{pessoa[0]} é menor de idade.')
print(f'\nDas 5 pessoas informadas, {tot_maior} eram maiores de idade e {tot_menor} eram menores de idade.')
