
def firstNotRepeatingChar(charSequence):
    seenLetters = {}

    for id, letter in enumerate(charSequence):
        if letter not in seenLetters:
            seenLetters[letter] = (id, 1)
        else:
            seenLetters[letter] = (seenLetters[letter][0], seenLetters[letter][1]  + 1)

    final_letters = []
    for key, value in seenLetters.iteritems():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    # Ordena los elementos con funcion lambda (funcion en una sola linea)
    notRepeatedLetters = sorted(final_letters, key = lambda value: value[1]) # es lo mismo que def function(value): return value[1]

    if notRepeatedLetters:
        return notRepeatedLetters[0][0]
    else:
        return '_'

if __name__ == '__main__':
    charSequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = firstNotRepeatingChar(charSequence)

    if result == '_':
        print('Todos los caracteres se repiten')
    else:
        print('El primer caracter no repetido es: {}'.format(result))