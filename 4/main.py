#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Crea un programa en Python que pida un número n al usuario, y a continuación cree una lista con las n palabras pedidas al usuario. Una vez creada la lista la imprimes en pantalla, y a continuación le pide al usuario dos palabras más pal1 y pal2. Se pide que cuente la cantidad de veces que aparece pal1 en la lista, y que reemplace con pal2 cada ocurrencia de pal1. Vuelve a mostrar la lista en pantalla. Por último elimina de la lista el elemento n-1 (sólo si n>1) y vuelve a mostrar la lista en pantalla.
# Salida del programa​:
# Introduzca la cantidad de palabras: 5
     
# Introduce la palabra 1: Pepe Introduce la palabra 2: Ordenador Introduce la palabra 3: Pepe Introduce la palabra 4: Tableta Introduce la palabra 5: Móvil
# Se imprime la lista:
# [‘Pepe’, ‘Ordenador’, ‘Pepe’, ‘Tableta’, ‘Móvil’]
# Introduce la palabra a buscar: Pepe
# Introduce la palabra para reemplazar: Computadora
# Se sustituye Pepe por Computadora, la lista queda así: [‘Computadora’, ‘Ordenador’, ‘Computadora’, ‘Tableta’, ‘Móvil’]
# Se elimina el elemento en la posición 4, la lista queda así: [‘Computadora’, ‘Ordenador’, ‘Computadora’, ‘Móvil’]

import sys
sys.path.append('../')

from printTools import PrintTools, Colors
PrintTools = PrintTools()
Colors = Colors()

def askToUser(msg):
    return raw_input(msg)

def getOccurrences(str, arr): 
    return [i for i, x in enumerate(words) if x == word1]

try:
    _n = int(askToUser('How many words would you like to enter?: '))
except ValueError:
    PrintTools.error('That\'s not a number')
    quit()

words = []

for n in range(_n):
    words.append(str(askToUser('Give the word #' + str(n) + ': ')))

PrintTools.emptyLine()
PrintTools.valueWithColor('First List: ', Colors.OKGREEN, words)

word1 = words[0]

occurrences = getOccurrences(word1, words)
PrintTools.valueWithColor('Occurences of "' + word1 + '": ' , Colors.WARNING, len(occurrences))
PrintTools.emptyLine()

for i in occurrences:
    words[i] = words[1]

PrintTools.valueWithColor('Second List: ', Colors.OKGREEN, words)
occurrences = getOccurrences(word1, words)
PrintTools.valueWithColor('Occurences of "' + word1 + '": ' , Colors.WARNING, len(occurrences))
PrintTools.emptyLine()

if(len(words) > 1):
    del words[len(words) - 1]

PrintTools.valueWithColor('Third List: ', Colors.OKGREEN, words)
