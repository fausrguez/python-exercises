#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Cuando un carácter es consecutivo en una cadena, es posible acortar el caracter reemplazando ese carácter con una cierta regla. Por ejemplo, en el caso del carácter X en la cadena XXXX, se expresa de la siguiente manera: #4X. Escribe un programa en Python que restaure la cadena original dada una cadena acortada.
# Aunque la cadena se introduzca en minúsculas, debe convertirse a mayúsculas.
# Salida del programa​:
# Introduzca una cadena acortada: XY#6Z1#4023
# La cadena original es la siguiente: XYZZZZZZ1000023

import sys
sys.path.append('../')

from printTools import PrintTools, Colors

PrintTools = PrintTools()
Colors = Colors()

def expandString(_str):
    fullStr = ''
    i = 0
    for n in range(len(_str)):
        try: 
            if _str[i] == '#':
                fullStr += str(_str[i + 2]).upper() * int(_str[i + 1])
                i += 3
            else:
                fullStr += str(_str[i]).upper()
                i += 1 
        except IndexError:
            continue

    PrintTools.valueWithColor('ShortString: ', Colors.HEADER, _str)
    PrintTools.valueWithColor('FullString: ', Colors.OKGREEN, fullStr)
    PrintTools.emptyLine()

expandString('XY#6Z1#4023')
