
amigos = list()
amigos.append('Pedro')
amigos.append('Enrique')
amigos.append('Alberto')

print(amigos)

# Accediendo a los elementos
print(amigos[0])

def averageTemps(temps):
    sumOfTemps = 0

    for temp in temps:
        sumOfTemps += float(temp)

    return sumOfTemps / len(temps)

if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = averageTemps(temps)
    print('La temperatura promedio es de {}'.format(average))