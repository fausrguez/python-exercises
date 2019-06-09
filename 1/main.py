#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Escribe un codigo Python que pida primero cuantos numeros se van a escribir, que pida a continuacioon esa cantidad de numeros y al final diga tanto la suma de los numeros pares introducidos como la suma de los numeros impares introducidos.
# Salida del programa​: Numeros a introducir: 4
# 2
# 5
# 3
# 8
# Suma de numeros impares: 5 Suma de numeros pares: 10

import sys
sys.path.append('../')

from printTools import PrintTools, Colors

PrintTools = PrintTools()
Colors = Colors()

def getNumber(msg, error):
   try:
      return int(raw_input(msg))
   except ValueError:
      PrintTools.error(error)
      return 0

def generateNumberList(n):
   arr = []
   for i in range(n):
      arr.append(getNumber('Give me the number #' + str(i) + ': ', 'That\'s not a number, so right now is a 0'))
   return arr

def makeSum(numbers):
   even = 0
   odd = 0
   for number in numbers: 
      if (number % 2) == 0:
         even += number  
      else: 
         odd += number
   PrintTools.emptyLine()
   PrintTools.valueWithColor('Sum of the even numbers: ', Colors.OKGREEN, str(even))
   PrintTools.valueWithColor('Sum of the odd numbers: ', Colors.OKGREEN, str(odd))

n = getNumber('How many numbers do you need to add together? ', 'That\'s not a number. Bye')
PrintTools.emptyLine()
numbers = quit() if n == 0 else generateNumberList(n)
numbers = filter(lambda value: value != 0, numbers)
makeSum(numbers)
