# -*- coding: utf-8 -*-

print(10 > 15 and 11 > 20)
print('a' == 'a' or 'b' != 'b')
print(not('a' == 'a'))
print(not True)

def sayHello(age):
    if age > 18:
        print('Hola señor')
    else:
        print('Hola niño')


if __name__ == '__main__':
    sayHello(18)