"""
mascota = 'loro'

if mascota == 'gato':
    print('Tenes un gato')
elif mascota == 'perro':
    print('Tenes un perro')
else:
    print('No se que animal tenes')

edad = 16
calificacion = 5

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:(
    print(f"{num2} es mayor que {num1}"))
else:
    print(f"{num1} y {num2} son iguales")


edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia== False:
        print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")

"""

habla_ingles = False
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
