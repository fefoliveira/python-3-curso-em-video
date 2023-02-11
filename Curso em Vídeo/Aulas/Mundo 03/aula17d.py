a = [1, 2, 3, 4, 5]
b = a  # Ligação das duas listas
b[2] = 8  # O 3 vira 8 tanto em "a" quanto em "b"
print(a)
print(b)
print()

a = [1, 2, 3, 4, 5]
b = a[:]  # Cópia da lista "a" na lista "b"
b[2] = 8  # Apenas o 3 da lista "b" vira 8
print(a)
print(b)
print()