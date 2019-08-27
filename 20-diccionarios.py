
miDiccionario = dict()
miDiccionario['primerElemento'] = 'Hola'
miDiccionario['segundoElemento'] = 'Adios'

print(miDiccionario['primerElemento'])

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['basesDeDatos'] = 10

# Se pueden obtener las key directamente
for key in calificaciones:
    print(key)

# Se pueden obtener los valores del diccionario
for value in calificaciones.values():
    print(value)

# Iteramos entre las llaves y los valores
for key, value in calificaciones.iteritems():
    print('llave: {}, valor: {}'.format(key, value))

# Sacamos el promedio
sumaCalificaciones = 0
for value in calificaciones.values():
    sumaCalificaciones += value

print('Su promedio es: {}'.format(float(sumaCalificaciones) / len(calificaciones)))