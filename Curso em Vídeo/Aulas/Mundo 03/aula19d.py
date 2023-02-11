estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input(f'Digite a {c+1}ª Unidade Federativa: ')).capitalize()
    estado['sigla'] = str(input(f'Digite a {c+1}ª sigla: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    print()
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
