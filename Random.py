## Importamos todas las libres con *
from random import *

"""

aleatorio = randint(0,10)
print(aleatorio)

## Valor decimal random
a = round(uniform(1,5),2)
print(a)

b = random()
print(b)

colores = ['azul', 'rojo', 'verde', 'rosa']
aleatorio1 = choice(colores)
print(aleatorio1)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)


Práctica Random 3
Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

"""

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)