
# listas
pares = []

# Ciclo que analiza del 1 al 30
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)

print(pares)

# Listas Comprehension (El mismo funcionamiento)

even = [num for num in range(1, 31) if num % 2 == 0]
print(even)

# Diccionario
cuadrados = {}

for num in range(1, 11):
    cuadrados[num] = num ** 2

print(cuadrados)

# Diccionario comprehension
squares = {num: num ** 2 for num in range(1, 11)}
print(squares)