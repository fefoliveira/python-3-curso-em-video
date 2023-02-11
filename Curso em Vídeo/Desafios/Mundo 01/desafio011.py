# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a suaárea e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
al = float(input('Qual a altura da sua parede, em metros? '))
la = float(input('E qual a largura, em metros? '))
a = al*la
print('A área dessa parede é de {:.2f}m², e você precisará de {:.1f}L de tinta para pintá-la completamente.'.format(a, a/2))
