"""
listas = ['a', 'b', 'c']

for letra in listas:
    ## Buscamos el indice de posicion de la lista y le sumamos 1 porque empieza a contar por 0
    n_letra = listas.index(letra) + 1
    print(f"Letra {n_letra}: {letra}")

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

palabra = 'python es genial'

for letra in palabra:
    print(letra)

for objeto in [[1,2],[3,4],[5,6],[7,8]]:
    print(objeto)

## Se guarda los valores en la posicion de las variables
for a,b in [[1,2],[3,4],[5,6],[7,8]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

## .items() nos permite mostras los valores dentro de los items
for item in dic.items():
    print(item)

for a,b in dic.items():
    print(a,b)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumnos in alumnos_clase:
    print('Hola ' + alumnos)



lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numeros in lista_numeros:
    suma_numeros = suma_numeros + numeros
    print(suma_numeros)

"""

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numeros in lista_numeros:
    if(numeros % 2 == 1):
        suma_impares = suma_impares + numeros
    else:
        suma_pares = suma_pares + numeros
print(f"Numeros impares: {suma_impares}")
print(f"Numeros pares: {suma_impares}")