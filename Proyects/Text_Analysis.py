
texto = input("Ingrese un texto: ")
letras = []

## Transformamos el texto en minuscula
texto = texto.lower()

## Utilizamos el metodo append con el input para agregar las letras que queremos almacenar
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("CANTIAD DE LETRAS")
## Contamos la cantidad de letras que hemos almacenados en 'letras'
cant_letras1 = texto.count(letras[0])
cant_letras2 = texto.count(letras[1])
cant_letras3 = texto.count(letras[2])

## Mosramos las letras contadas
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cant_letras1} veces.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cant_letras2} veces.")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cant_letras3} veces.")

print("\n")
print("CANTIAD DE PALABRAS")
## Creamos una varaible que contenga las palabras
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)}.")

print("\n")
print("LETRAS DE INICIO Y DEL FIN")

## Al ser un dato string, buscamos el primer caracter del texto
letra_inicio = texto[0]
## Conteo inverso
lera_final = texto[-1]
print(f"La letra inicial es {letra_inicio} y la final es {lera_final}.")

print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
## Unimos las palabras de las listas
texto_invertido = ' '.join(palabras)
print(f"El texto invertido: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")

buscar_python = 'python' in texto
## Creamos un diccionario para adapttar los valores booleanos
dic = {True: "Si", False: "No" }

## Busco en el diccionario para mostrar el dato guardado
print(f"Existe la palabra 'Python?' {dic[buscar_python]} se encuentra en el texto.")






