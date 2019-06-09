# Ejercicios básicos de programación Python (no orientado a objetos)
## 1. Escribe un código Python que pida primero cuántos números se van a escribir, que pida a continuación esa cantidad de números y al final diga tanto la suma de los números pares introducidos como la suma de los números impares introducidos.
Salida del programa​: Números a introducir: 4
    2
    5
    3
    8
Suma de números impares: 5 Suma de números pares: 10
## 2. Escribe un código Python que simule un juego en el que dos jugadores (Pepe y María) sacan tres cartas al azar del 1 al 10. Gana el jugador que saque la mayor puntuación total, siempre que no se pase de quince, en cuyo caso el jugador pierde siempre. Los jugadores pueden empatar.
Salida del programa​:
Pepe juega y saca las cartas: 5, 2, 10 María juega y saca las cartas: 2, 4, 8 Gana María con 14 puntos
## 3. Cuando un carácter es consecutivo en una cadena, es posible acortar el caracter reemplazando ese carácter con una cierta regla. Por ejemplo, en el caso del carácter X en la cadena XXXX, se expresa de la siguiente manera: #4X. Escribe un programa en Python que restaure la cadena original dada una cadena acortada.
Aunque la cadena se introduzca en minúsculas, debe convertirse a mayúsculas.
Salida del programa​:
Introduzca una cadena acortada: XY#6Z1#4023
La cadena original es la siguiente: XYZZZZZZ1000023
## 4. Crea un programa en Python que pida un número n al usuario, y a continuación cree una lista con las n palabras pedidas al usuario. Una vez creada la lista la imprimes en pantalla, y a continuación le pide al usuario dos palabras más pal1 y pal2. Se pide que cuente la cantidad de veces que aparece pal1 en la lista, y que reemplace con pal2 cada ocurrencia de pal1. Vuelve a mostrar la lista en pantalla. Por último elimina de la lista el elemento n-1 (sólo si n>1) y vuelve a mostrar la lista en pantalla.
Salida del programa​:
Introduzca la cantidad de palabras: 5
     
 Introduce la palabra 1: Pepe Introduce la palabra 2: Ordenador Introduce la palabra 3: Pepe Introduce la palabra 4: Tableta Introduce la palabra 5: Móvil
Se imprime la lista:
[‘Pepe’, ‘Ordenador’, ‘Pepe’, ‘Tableta’, ‘Móvil’]
Introduce la palabra a buscar: Pepe
Introduce la palabra para reemplazar: Computadora
Se sustituye Pepe por Computadora, la lista queda así: [‘Computadora’, ‘Ordenador’, ‘Computadora’, ‘Tableta’, ‘Móvil’]
Se elimina el elemento en la posición 4, la lista queda así: [‘Computadora’, ‘Ordenador’, ‘Computadora’, ‘Móvil’]

# Ejercicios de programación Python (Orientado a objetos)
## 1. Diseña y programa una clase Persona que contenga lo siguiente:
    ● Sus propiedades o atributos son: ​nombre, edad, NIF, peso y altura​. Crea métodos para acceder a estas propiedades, que serán privadas, ocultas desde fuera de la clase, por eso hay que crear los métodos necesarios para acceder al valor de estas y también para modificarlas. Por ejemplo: getNIF() y setNIF(“12345678A”). Puedes añadir algún atributo o propiedad que necesites.
    ● Todas las propiedades excepto el NIF contendrán valores por defecto: 0 para valores numéricos, “” para cadenas, etc. El NIF debe ser una cadena alfanumérica de 9 caracteres.
    ● Crea un ​constructor ​al que se le pase obligatoriamente el nombre y la edad, el resto de datos son opcionales y si no se pasan por parámetro se establecen por defecto.
    ● Los ​métodos ​que se crearán son:
        - calcularIMC():​ este método calcula si la persona está en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que está por debajo de su peso ideal la función devuelve un 0, y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1. Usa constantes para devolver estos valores. 
        - e​sMayorDeEdad()​: indica si es mayor de edad, devuelve un booleano. print()​: devuelve en pantalla toda la información del objeto de tipo Persona. 
        - generaNIF():​ generaunnúmeroaleatoriode8cifrasnuméricas,ygeneraa partir de este su número su letra correspondiente. Este método es invocado cuando se construya el objeto. Será un método no accesible desde fuera dela clase. Busca en Internet como se calcula la letra del NIF. En el método setNIF comprueba que el NIF que se pasa sea válido.
Después de haber creado la clase anterior, crea un fragmento de código que haga lo siguiente:
    ● Pide por teclado el nombre, la edad, el peso y la altura.
    ● Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores
    variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura, y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
    ● Para cada objeto, debe comprobar si está en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
    ● Indicar para cada objeto si es mayor de edad.
    ● Por último, mostrar la información de cada objeto.