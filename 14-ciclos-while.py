import random

i = 0

while i < 10:
    print(i)
    i += 1

i = 0
while i >= 15:
    print(i)
    i += 1 


def run():
    numberFound = False
    randomNumber = random.randint(0, 20)

    while not numberFound:
        number = int(raw_input('Intenta un numero: '))

        if number == randomNumber:
            print('Felicidades, encontraste el numero')
            numberFound = True
        elif number > randomNumber:
            print('El numero es mas pequenio')
        else:
            print('El numero es mas grande')

if __name__ == '__main__':
    run()