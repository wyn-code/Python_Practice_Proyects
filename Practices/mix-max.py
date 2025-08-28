"""
menor = min(58,97,32,12)
mayor = max(58,97,32,12)
print(menor)
print(mayor)

lista = [58,76,32,12]
print(f'El menor es: {min(lista)} y el mayor es: {max(lista)}')

nombres = ['Juan', 'Diego', 'Alicia']
print(min(nombres))

name = 'Carlos'
print(min(name))

dic = {'C1': 45, 'C2': 40, 'C3': 30, 'C4': 20}
## Busca por orden alfabetico
print(max(dic))

## Busca por orden de los valores
print(min(dic.values()))


Práctica Min y Max 1
Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]



lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_max = max(lista_numeros)
print(valor_max)


Práctica Min y Max 2
Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]


lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rangos = max(lista_numeros) - min(lista_numeros)
print(rangos)


Práctica Min y Max 3
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

"""

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
nombre = max(diccionario_edades)
print(f"{nombre} y tiene {edad_minima}")
