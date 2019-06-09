#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 1. Diseña y programa una clase Persona que contenga lo siguiente:
# ● Sus propiedades o atributos son: ​nombre, edad, NIF, peso y altura​. Crea métodos para acceder a estas propiedades, que serán privadas, ocultas desde fuera de la clase, por eso hay que crear los métodos necesarios para acceder al valor de estas y también para modificarlas. Por ejemplo: getNIF() y setNIF(“12345678A”). Puedes añadir algún atributo o propiedad que necesites.
# ● Todas las propiedades excepto el NIF contendrán valores por defecto: 0 para valores numéricos, “” para cadenas, etc. El NIF debe ser una cadena alfanumérica de 9 caracteres.
# ● Crea un ​constructor ​al que se le pase obligatoriamente el nombre y la edad, el resto de datos son opcionales y si no se pasan por parámetro se establecen por defecto.
# ● Los ​métodos ​que se crearán son:
# calcularIMC():​ este método calcula si la persona está en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que está por debajo de su peso ideal la función devuelve un 0, y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1. Usa constantes para devolver estos valores. e​sMayorDeEdad()​: indica si es mayor de edad, devuelve un booleano. print()​: devuelve en pantalla toda la información del objeto de tipo Persona. generaNIF():​ generaunnúmeroaleatoriode8cifrasnuméricas,ygeneraa partir de este su número su letra correspondiente. Este método es invocado cuando se construya el objeto. Será un método no accesible desde fuera de
# la clase. Busca en Internet como se calcula la letra del NIF. En el método setNIF comprueba que el NIF que se pasa sea válido.
# Después de haber creado la clase anterior, crea un fragmento de código que haga lo siguiente:
# ● Pide por teclado el nombre, la edad, el peso y la altura.
# ● Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores
# variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura, y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
# ● Para cada objeto, debe comprobar si está en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
# ● Indicar para cada objeto si es mayor de edad.
# ● Por último, mostrar la información de cada objeto.

import re
import random

import sys
sys.path.append('../../')

from printTools import PrintTools, Colors
PrintTools = PrintTools()
Colors = Colors()

class NifError(Exception):
    pass

class NoNumberError(Exception):
    pass

class Person:
    __imcResults = ["avarage", "overweight", "underweight"]

    def __init__(self, name, age, weight=0, height=0):
        self.__attributes = {
            "name" : '',
            "age" : 0,
            "nif" : '',
            "weight" : 0,
            "height" : 0
        }

        values = locals()
        del values['self']
        for key in values:
            self.setAttr(key, values[key])
        if(self.__attributes['nif'] == ''):
            self.__attributes['nif'] = self.__genNif()

    def setAttr(self, key, value):
        try:
            if(key in ['age', 'weight', 'height']):
                if(type(value) != int):
                    raise NoNumberError
            if(key == 'nif'):
                value = value.upper()
                if (not bool(re.match("[0-9]{8}[A-Z]", value)) or self.__getLetterNif(value) == value[:-1]):
                    raise NifError
            self.__attributes[key] = value if type(value) == int else value
        except KeyError:
            PrintTools.error('The Key doesn\'t exist')
        except NoNumberError:
            PrintTools.error(key.upper() + ' value is not a number, now it\'s 0')
        except NifError:
            PrintTools.error('NIF value not valid')

    def getAttr(self, key):
        try:
            return self.__attributes[key]
        except KeyError:
            return 'The Key does\'nt exist'

    def __getIMC(self):
        weight = self.getAttr('weight')
        height = float(self.getAttr('height'))/100
        imc = round(weight/height ** 2, 0)

        if(imc < 20):
            return -1
        elif(imc > 25):
            return 1
        else:
            return 0

    def __isAdult(self): 
        return self.__attributes['age'] >= 18

    def __genNif(self):
        numbers = range(0,9)
        number = ''.join(str(random.choice(numbers)) for i in range(8))
        return  number + self.__getLetterNif(number)

    def __getLetterNif(self, value):
        keys = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return keys[int(value[:8]) % 23]

    def __str__(self):
        PrintTools.msgWithColor('Data of ' + self.getAttr('name') + ':', Colors.HEADER + Colors.UNDERLINE)
        PrintTools.valueWithColor('Name: ', Colors.OKGREEN, self.getAttr('name'))
        PrintTools.valueWithColor('Age: ', Colors.OKGREEN, str(self.getAttr('age')) + ' years old')
        PrintTools.valueWithColor('Is adult: ', Colors.OKGREEN, 'Yes' if self.__isAdult() else 'No')
        PrintTools.valueWithColor('NIF: ', Colors.OKGREEN, self.getAttr('nif'))
        if(self.getAttr('weight') > 0):
            PrintTools.valueWithColor('Weight: ', Colors.OKGREEN, str(self.getAttr('weight')) + ' Kg')
            PrintTools.valueWithColor('Height: ', Colors.OKGREEN, str(self.getAttr('height')) + ' cm')
            PrintTools.valueWithColor('IMC: ', Colors.OKGREEN, self.__imcResults[self.__getIMC()])
        return ''


persons = []

def newPerson():
    try: 
        return Person(
            raw_input('Give me the person\'s name: '),
            int(raw_input('Give the person\'s age: ')),
            int(raw_input('How heavy is he/she?(Kg): ')),
            int(raw_input('How tall is he/she?(cm): ')))
    except ValueError:
        PrintTools.error('That\'s not a correct value')
        return ''

persons.append(newPerson())
PrintTools.emptyLine()

persons.append(Person('Pepe', 40))

persons.append(Person('María', 18))

persons[2].setAttr('weight', 45)
persons[2].setAttr('height', 159)

for person in persons:
    print(str(person)) 