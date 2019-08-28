# -- coding: utf-8 --

# Funcion decorador
def decorador(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper

# Se le asigna la funcion decoradora
@decorador
def protectedFunc():
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))
    
    # Decorador
    protectedFunc(password)