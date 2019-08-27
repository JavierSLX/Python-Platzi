myString = 'platzi'
name = 'JAVIER'

# Acceder a un caracter
print(myString[5])

# El largo de una cadena
print(len(myString))

# Convierte en mayuscula
print(myString.upper())

# Checa si es mayuscula
print(name.isupper())

# Convierte en minuscula
print(name.lower())

# Checa si es minuscula
print(myString.islower())

# Checa si existe un caracter en la cadena
print(myString.find('a'))

# Checa si el caracter es un digito
print(myString.isdigit())

# Checa si la cadena termina con un caracter en especial
print(myString.endswith('i'))

# Checa si la cadena comienza con un caracter en especial
print(myString.startswith('a'))

# Separa la cadena a partir de uno de sus caracteres
print(myString.split('t'))

# Separa cada caracter con un simbolo especial
print('-'.join(myString))