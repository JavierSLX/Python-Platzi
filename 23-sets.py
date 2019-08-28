# Los sets es como usar conjuntos

s = set([1, 2, 3])
t = set([3, 4, 5])

# Operaciones con sets
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))

# Saber si un elemento pertenece al set
print(1 in s)
print(1 in t)
print(1 not in s)
print(1 not in t)