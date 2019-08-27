# -*- coding: utf-8 -*-

# Parte la cadena original para formar una nueva
s = 'hola'
r = 'l' + s[1:]
print(r)

nombre1 = 'lola'
nombre2 = 'joaquín'

print(nombre1 > nombre2)

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)

if __name__ == '__main__':
    number = int(raw_input('Escribe un numero: '))
    result = factorial(number)
    print(result)