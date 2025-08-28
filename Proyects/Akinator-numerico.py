from random import *

nombre_jugador = input("Bienvenido al adivinador de numeros, dime tu nombre: ")
numero_secreto = randint(1,100)
cont = int(8)
numero_jugador = 0

print(f"Bienvenido {nombre_jugador}, he pensado un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cual crees que es el numero.")

while cont > 0:
    numero_jugador = int(input(f"Tenes {cont}." + "\nIngrese el numero de jugador: "))
    if  numero_jugador not in range(1,101):
        cont -= 1
        print("Elegiste un numero no permitido.")
    elif numero_jugador < numero_secreto:
        cont -= 1
        print("Es incorrecto, elegiste un número menor al número secreto.")
    elif numero_jugador > numero_secreto:
        cont -= 1
        print("Es incorrecto, elegiste un número mayor al número secreto.")
    else:
        print(f"Ganaste! Con un total de {cont} intentos.")
        break

    if cont == 0 and numero_jugador != numero_secreto:
        print(f"Te quedaste sin intentos. El número secreto era {round(numero_secreto, 2)}.")







