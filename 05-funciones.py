# -*- coding: utf-8 -*-

import turtle

def main(): #Define la funcion
    window = turtle.Screen()
    dave = turtle.Turtle()

    makeSquare(dave)
    turtle.mainloop()

def makeSquare(dave):
    length = int(raw_input('Tamaño de cuadrado: '))

    for i in range(4):
        makeLineAndTurn(dave, length)

def makeLineAndTurn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()