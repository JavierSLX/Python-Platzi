
def escritura():
    # Abre un archivo y escribe los numeros en el documento
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def lectura():
    # Lee un archivo
    counter = 0
    with open('pais.txt', 'r') as f:
        for line in f:
            counter += line.count('lengua')

    print('La palabra lengua se encuentra {} veces en el texto'.format(counter))



if __name__ == "__main__":
    lectura()