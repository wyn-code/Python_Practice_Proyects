"""
monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    ## -= es lo mismo que monedas - 1
    monedas -= 1
else: print("No tengo mas dinero.")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Queres seguir? (s/n)")
else:
    print("Gracias")



respuesta = 's'

while respuesta == 's':
    ## Su funcion es guardar el lugar para poder seguir codeando con otras funciones
    pass

print("hola")



nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)


numero = 10

while numero > -1:
    print(numero)
    numero -= 1


numero = 50

while numero > -1:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

"""

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)


