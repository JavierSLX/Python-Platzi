print(range(5))
print(range(5, 40, 3))

# Ciclo for
for i in range(5):
    print(i)

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i ** 2)

for i in range(30):
    if i % 3 == 0:
        print(i ** 2)
    elif i == 22:
        break

r = 'ferrocarril'
for letter in r:
    print(letter)