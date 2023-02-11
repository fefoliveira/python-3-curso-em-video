pessoas = {'nome': 'Fernando', 'sexo': 'M', 'idade': 20}
for k in pessoas.keys():
    print(k)

print()
for k in pessoas.values():
    print(k)

print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['nome'] = 'Duda'
pessoas['idade'] = '17'
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['peso'] = 64
for k, v in pessoas.items():
    print(f'{k} = {v}')