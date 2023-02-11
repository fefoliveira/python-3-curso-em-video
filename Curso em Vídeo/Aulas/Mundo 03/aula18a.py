teste = list()
teste.append('Fernando')
teste.append('20')
galera = list()
galera.append(teste[:])
teste[0] = 'Duda'
teste[1] = 17
galera.append(teste[:])
print(galera)
