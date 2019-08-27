
miLista = []
print(type(miLista))

# Agregar un elemento
miLista.append(1)
print(miLista)

# Suma de listas
miLista2 = [2, 3, 4]
miLista3 = miLista + miLista2
print(miLista3)

# Multiplicando listas
miLista4 = ['a']
miLista5 = miLista4 * 10
print(miLista5)

# Invertir lista
print(miLista3[::-1])

utiles = ['lapiz', 'calculadora', 'cuaderno']

# Borra el primer elemento
del utiles[0]
print(utiles)

casa = 'casa'
print('{}'.format(casa))
listaCasa = list(casa)
print(listaCasa)

print(''.join(listaCasa))