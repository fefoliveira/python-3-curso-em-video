'''Análise'''

frase = 'Curso em Vídeo Python'
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.count('O'))
print(frase.upper().count('O'))

print(frase.find('deo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.find('Android'))
print('Curso' in frase)
print('Android' in frase)

frase2 = '   Curso em Vídeo Python   '
print(len(frase2))
print(len(frase2.strip()))




