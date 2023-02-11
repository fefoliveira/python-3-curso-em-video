def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 34, 9, 1, 0, 2]
dobra(valores)
print(valores)
