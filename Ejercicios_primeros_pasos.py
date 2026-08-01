# Escribir un programa que realice la siguiente operacioón aritmetica
#((3+2)/(2*5))^2

#FALTA MEJORAR COSAS

print("Ejercicio 1 - FALTAN MEJORAR COSAS\n")
def funcion(lista):
    #lista_enumerada = enumerate(lista)
    #Se tiene una variable para tener un control del indice de la lista
    #Nos serivara para podernos movernos atravez de la lista
    movimiento = 0
    #Ciclo en cargado de movernos
    while movimiento <= len(lista) -1:
        #Si se detecta un caracter de oepracion, se entiende que debe realizar dicha operacion
        if lista[movimiento] in ("+", "-", "*"):
            #Almacena los numeros anteriores y posteriores para realizar las operaciones
            num1 = int(lista[movimiento-1])
            num2 = int(lista[movimiento+1])
            match lista[movimiento]:
                #Operacion suma
                case "+":
                    resultado = num1 + num2
                #Operacion resta
                case "-":
                    resultado = num1 - num2
                #Operacion multiplicacion
                case "*":
                    resultado = num1 * num2
                #En caso de error
                case _:
                    print("Error")
        #Si se detecta la division, se almacena el resultado de la primera operacion
        elif lista[movimiento] in ("/"):
            resultado1 = resultado
        #Si se detecta la potencia, se almacena el valor de la potencia de acuerdo al numero que se encuentra en la posicion siguiente
        elif lista[movimiento] in ("^"):
            potencia = int(lista[movimiento + 1])
        #Avanzamos
        movimiento +=1
    #Realizamos la operacion final de acuerdo a los resultados obtenidos
    return float(pow((resultado1 / resultado), potencia))

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
        lista.append(acumulado)
        lista.append(caracter)
        acumulado = ""
    

print(funcion(lista))