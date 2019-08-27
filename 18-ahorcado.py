# -*- coding: utf-8 -*-

import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''
    
    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''
    
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

# Funcion que regresa una palabra aleatoria
def randomWord():
    id = random.randint(0, len(WORDS) - 1)
    return WORDS[id]

def displayBoard(hiddenWord, tries):
    print(IMAGES[tries] + '\n')
    print(hiddenWord)
    print('--- * --- * --- * --- * --- * ---')

def run():
    word = randomWord()
    hiddenWord = ['-'] * len(word)
    tries = 0

    while True:
        displayBoard(hiddenWord, tries)
        currentLetter = str(raw_input('Escoge una letra: '))

        letterIndexes = []
        for i in range(len(word)):
            if word[i] == currentLetter:
                letterIndexes.append(i)

        if len(letterIndexes) == 0:
            tries += 1

            # Checa si perdio el jugador
            if tries == len(IMAGES) - 2:
                displayBoard(hiddenWord, tries)
                print('\nLo sentimos, perdiste. La palabra correcta era {}'.format(word))
                break
        else:
            for id in letterIndexes:
                hiddenWord[id] = currentLetter

            letterIndexes = []

        # Chea si gano el jugador
        try:
            hiddenWord.index('-')
        except ValueError:
            print('\nFelicidades. Ganaste. La palabra es: {}'.format(word))
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()