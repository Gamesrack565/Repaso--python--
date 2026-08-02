# Escribir un programa que realice la siguiente operacioón aritmetica
#((3+2)/(2*5))^2

#Calculadora funciona con entrada de numeros enteros
#Falta mejorar
#Falta que pueda recibir numeros flotantes

print("Ejercicio 1 - FALTAN MEJORAR COSAS\n")

def parentesis(lista):
    movimiento = 0
    while movimiento <= len(lista)-1:
        if 0 <= movimiento < len(lista) and lista[movimiento] == ")":
            for ind in range(movimiento, -1,-1):
                if lista[ind] == "(":
                    operacion = lista[ind+1: movimiento]
                    resultado = funcion(operacion)
                    lista[ind:movimiento+1] = [resultado]
                    movimiento = 0
                    break
        else:
            movimiento +=1

    return funcion(lista)


def funcion(lista):
    #lista_enumerada = enumerate(lista)
    #Se tiene una variable para tener un control del indice de la lista
    #Nos serivara para podernos movernos atravez de la lista
    movimiento = 0
    #Ciclo en cargado de movernos
    while movimiento <= len(lista) -1:
        
        if lista[movimiento] == "^":
            resultado = float(lista[movimiento-1]) ** float(lista[movimiento+1])
            lista[movimiento-1:movimiento+2] = [resultado]
            print(f"potencia: {lista}")
            movimiento = 0

        else:
            movimiento +=1

    movimiento = 0
    while movimiento <= len(lista) -1:
        if lista[movimiento] in ("*", "/"):
            match lista[movimiento]:
                case "*":
                    resultado = float(lista[movimiento-1]) * float(lista[movimiento+1])
                    lista[movimiento-1:movimiento+2] = [resultado]
                    print(f"multiplicacion: {lista}")
                case "/":
                    resultado = float(lista[movimiento-1]) / float(lista[movimiento+1])
                    lista[movimiento-1:movimiento+2] = [resultado]
                    print(f"division: {lista}")
                case _:
                    print("Error")
            movimiento = 0

        else:
            movimiento +=1

    movimiento = 0
    while movimiento <= len(lista) -1:
        if lista[movimiento] in ("+", "-"):
            match lista[movimiento]:
                #Operacion suma
                case "+":
                    resultado = float(lista[movimiento-1]) + float(lista[movimiento+1])
                    lista[movimiento-1:movimiento+2] = [resultado]
                    print(f"suma: {lista}")
                #Operacion resta
                case "-":
                    resultado = float(lista[movimiento-1]) - float(lista[movimiento+1])
                    lista[movimiento-1:movimiento+2] = [resultado]
                    print(f"resta: {lista}")
                case _:
                    print("Error")
            movimiento = 0

        else:
            movimiento +=1

    #Realizamos la operacion final de acuerdo a los resultados obtenidos
    return float(lista[0])

#Se tiene una lista vacia para almacenar los valores que se ingresen
lista = []
print("Ingresa tus valores:")
#Se pide la operacion en una sola linea, y se eliminan los espacios para poder separar los valores
valor = input(": ")
acumulado = ""
for caracter in valor.replace(" ", ""):
    #Si se detecta el signo de igual, se entiende que la operacion ha terminado y se agrega el ultimo valor a la lista
    if caracter == "=":
        lista.append(acumulado)
        acumulado = ""
        break
    #Si se detecta un caracter numerico, se va acumulando en una variable para poder formar el numero completo
    elif caracter.isdigit():
        acumulado += caracter
    #Si se detecta un caracter de operacion, se agrega el numero acumulado y el caracter a la lista, y se reinicia la variable acumulado
    else:
        if not acumulado == "":
            lista.append(acumulado)
        
        lista.append(caracter)
        acumulado = ""

if not acumulado == "":
    lista.append(acumulado)

print(lista)
print(parentesis(lista))


