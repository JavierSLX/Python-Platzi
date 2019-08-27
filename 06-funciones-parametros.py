# -*- coding: utf-8 -*-

def main():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos\n')

    ammount = float(raw_input('Ingresar pesos mexicanos: '))

    result = foreignChangeCalculator(ammount)
    print('${} mexicanos son ${} colombianos'.format(ammount, result))


def foreignChangeCalculator(ammount):
    mexToColRate = 145.97
    return mexToColRate * ammount

if __name__ == '__main__':
    main()