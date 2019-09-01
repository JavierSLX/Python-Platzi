def sumaRecursiva(suma, n):

    if n == 0:
        return suma
    else:
        suma += n
        return sumaRecursiva(suma + n, n - 1)

if __name__ == '__main__':
    print('SUMA RECURSIVA')
    print(sumaRecursiva(0, 10))