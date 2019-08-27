
# Busqueda binaria
def binarySearch(numbers, numberToFind, low, high):
    
    # Cuando se cruzan los indices indicando que no se encontro el numero
    if low > high:
        return False

    mid = (low + high) / 2

    # Usando la funcion recursiva para encontrar el numero
    if numbers[mid] == numberToFind:
        return True
    elif numbers[mid] > numberToFind:
        return binarySearch(numbers, numberToFind, low, mid - 1)
    else:
        return binarySearch(numbers, numberToFind, mid + 1, high)

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numberToFind = int(raw_input('Ingresa un numero: '))
    result = binarySearch(numbers, numberToFind, 0, len(numbers) - 1)

    if result is True:
        print('El numero si esta en la lista')
    else:
        print('El numero NO esta en la lista')