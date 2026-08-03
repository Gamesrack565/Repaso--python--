#Inicio del ejercicio:
#Escribir un programa que realice la siguiente operacioón aritmetica
#((3+2)/(2*5))^2

#Resultado final:
#Calculadora funcionaL básica, realiza sumas, restas, divisiones, multiplicaciones y potencias
#Con números decimales y parentesis, siguiendo la jerarquia de operaciones


#Librerias utilizadas
#Os: Para limpiar la pantalla
import os
#Difflib: Para poder detectar si el usuario desea salir del programa
#Especificamente hace una comparacion de cadenas y nos dice si son similares o no, dependiendo de un porcentaje que le indiquemos
from difflib import get_close_matches

#Funcion principal "CALCULADORA"
def calculadora(valor):
    """
    Se encarga de procesar la operación de entrada y realiza el llamado de las funciones para procesar
    numeros decimales, detetcar parentesis y realizar las operaciones.
    """
    #Se tiene una lista vacia para almacenar los valores que se ingresen
    lista = []

    acumulado = ""
    for caracter in valor.replace(" ", ""):
        #Si se detecta el signo de igual, la operacion ha terminado
        if caracter == "=":
            lista.append(acumulado)
            acumulado = ""
            break
            
        #1- Es un número o un punto decimal, se acumula en la variable "acumulado"
        elif caracter.isdigit() or caracter == ".":
            acumulado += caracter
            
        #2- Es un signo de menos, y es el primer caracter o viene despues de un signo matemático, se acumula en la variable "acumulado"
        elif caracter == "-" and acumulado == "" and (len(lista) == 0 or lista[-1] in ("(", "+", "-", "*", "/", "^")):
            acumulado += caracter
            
        #3- Es un signo matemático, se agrega a la lista y se reinicia la variable "acumulado"
        else:
            if not acumulado == "":
                lista.append(acumulado)
            
            lista.append(caracter)
            acumulado = ""

    # Red de seguridad final
    if not acumulado == "":
        lista.append(acumulado)

    #Verifica parentesis y realiza las operaciones de acuerdo al orden
    resultado = parentesis(lista)
    
    #Regresa el resultado
    return resultado

#Segunda función principal encargada de identificar parentesis
def parentesis(lista):
    """
    Funcion encargada de identificar parentesis y su contenido que tienen
    Esto para seguir la jerarquia de operaciones
    Al identificar su contenido, manda las operación a la funcion "funcion" y devuelve el resultado
    """
    #Variable encargada de recorrer la lista
    movimiento = 0
    #Ciclo encargado de recorrer la lista y verificar si hay parentesis
    while movimiento <= len(lista)-1:
        if 0 <= movimiento < len(lista) and lista[movimiento] == ")":
            #En caso de encontrar un parentesis de cierre, se recorre la lista hacia atras para encontrar el parentesis de apertura correspondiente
            for ind in range(movimiento, -1,-1):
                if lista[ind] == "(":
                    #En caso de encontrar un parentesis de apertura, se crea una nueva lista con el contenido entre los parentesis
                    operacion = lista[ind+1: movimiento]
                    #Se manda la operación a la funcion "funcion" para que realice las operaciones correspondientes
                    resultado = funcion(operacion)
                    #Se remplaza el contenido entre los parentesis por el resultado de la operación
                    lista[ind:movimiento+1] = [resultado]
                    movimiento = 0
                    break
        else:
            #Si no se encuentra un parentesis de cierre, se sigue recorriendo la lista
            movimiento +=1

    #Se regresa la lista con los valores ya procesados
    return funcion(lista)

#Funcion capaz de resolver las oepraciones
def funcion(lista):
    #Se tiene una variable para tener un control del indice de la lista
    #Nos serivara para podernos movernos atravez de la lista
    movimiento = 0
    #Ciclo en cargado de movernos
    while movimiento <= len(lista) -1:
        #Si se encuentra un signo de potencia, se realiza la operación correspondiente
        if lista[movimiento] == "^":
            #Se realiza la operación de potencia y se remplaza el contenido de la lista por el resultado
            resultado = float(lista[movimiento-1]) ** float(lista[movimiento+1])
            #Se remplaza el contenido de la lista por el resultado
            lista[movimiento-1:movimiento+2] = [resultado]
            #print(f"potencia: {lista}")
            movimiento = 0
        else:
            movimiento +=1

    movimiento = 0
    #Ciclo encargado de recorrer la lista y verificar si hay multiplicaciones o divisiones
    while movimiento <= len(lista) -1:
        if lista[movimiento] in ("*", "/"):
            match lista[movimiento]:
                #Operacion multiplicacion
                case "*":
                    #Se realiza la operación de multiplicación y se remplaza el contenido de la lista por el resultado
                    resultado = float(lista[movimiento-1]) * float(lista[movimiento+1])
                    #Se remplaza el contenido de la lista por el resultado
                    lista[movimiento-1:movimiento+2] = [resultado]
                    #print(f"multiplicacion: {lista}")
                #Operacion division
                case "/":
                    try:
                        #Se realiza la operación de división y se remplaza el contenido de la lista por el resultado
                        resultado = float(lista[movimiento-1]) / float(lista[movimiento+1])
                        #Se remplaza el contenido de la lista por el resultado
                        lista[movimiento-1:movimiento+2] = [resultado]
                        #print(f"division: {lista}")
                    except ZeroDivisionError as e:
                        return print(f"Error: {e}")
                case _:
                    print("Error")
            movimiento = 0

        else:
            movimiento +=1

    movimiento = 0
    #Ciclo encargado de recorrer la lista y verificar si hay sumas o restas
    while movimiento <= len(lista) -1:
        if lista[movimiento] in ("+", "-"):
            match lista[movimiento]:
                #Operacion suma
                case "+":
                    #Se realiza la operación de suma y se remplaza el contenido de la lista por el resultado
                    resultado = float(lista[movimiento-1]) + float(lista[movimiento+1])
                    #Se remplaza el contenido de la lista por el resultado
                    lista[movimiento-1:movimiento+2] = [resultado]
                    #print(f"suma: {lista}")
                #Operacion resta
                case "-":
                    #Se realiza la operación de resta y se remplaza el contenido de la lista por el resultado
                    resultado = float(lista[movimiento-1]) - float(lista[movimiento+1])
                    #Se remplaza el contenido de la lista por el resultado
                    lista[movimiento-1:movimiento+2] = [resultado]
                    #print(f"resta: {lista}")
                case _:
                    print("Error")
            movimiento = 0

        else:
            movimiento +=1

    #Realizamos la operacion final de acuerdo a los resultados obtenidos
    return float(lista[0])


print("=======================================================================")
print("\tEjercicio 1 - CALCULADORA\n")
print("=======================================================================")
print("Calculadora funcionaL básica, realiza sumas, restas, divisiones, multiplicaciones y potencias")
print("Con números decimales y parentesis, siguiendo la jerarquia de operaciones")
print("----> Si de sea salir del programa escriba 'salir' <----\n")

while True:
    print("Ingresa tus valores:")
    #Se pide la operacion en una sola linea
    valor = input(": ").lower().strip() 

    comandos_salida = ["salir", "exit"]

    es_salida = get_close_matches(valor, comandos_salida, n=1, cutoff=0.5)

    #Se verifica si el usuario desea salir del programa
    if len(es_salida) > 0 or valor == "s":
        os.system("cls")
        print("=========================")
        print("Saliendo del programa...")
        print("=========================")
        print("By: Angel A Higuera")
        break
    #En caso de que no se desee salir del programa, se realiza la operación correspondiente
    else:
        resultado = calculadora(valor)
        print(f"=: {resultado}\n")