#Ejercicio de cadenas

#Crear un programa, que tenga una variable con la cadena "Te quiero solo como amigo", y muestre la siguiente información:
#   Imprima los dos primeros caracteres.
#   Imprima los tres últimos caracteres.
#   Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera "recta" debería imprimir rca
#   Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
#   Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es "reflejo" imprime reflejoojelfer.
# cadena = "recta"

cadena = "Te quiero solo como amigo"

# Imprimir los dos primeros caracteres:
dos_caracteres = cadena[0:2]
print(dos_caracteres)
ultimos_tres = cadena[len(cadena)-3:len(cadena)]
print(ultimos_tres)

cada_dos_caracters = cadena[0:len(cadena):2]
print(cada_dos_caracters)

reverse = cadena[::-1]
print(reverse)

reflejo = cadena + reverse
print(reflejo)