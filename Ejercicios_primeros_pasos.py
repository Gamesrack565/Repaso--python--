#Inicio del ejercicio:
#Escribir un programa que realice la siguiente operacioón aritmetica
#((3+2)/(2*5))^2

#Resultado final:
#Calculadora funcionaL básica, realiza sumas, restas, divisiones, multiplicaciones y potencias
#Con números decimales y parentesis, siguiendo la jerarquia de operaciones



#Funcion principal "CALCULADORA"
def calculadora():
    """
    Se encarga de procesar la operación de entrada y realiza el llamado de las funciones para procesar
    numeros decimales, detetcar parentesis y realizar las operaciones.
    """
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

    #Se recorre la lista para agregar números decimales, si no hay se regresa la lista normal
    lista = agregar_decimal(lista)
    #Verifica parentesis y realiza las operaciones de acuerdo al orden
    lista = parentesis(lista)
    #Regresa el resultado en formato flotante
    return float(lista[0])

#Funcion que verifica si hay decimales
def agregar_decimal(lista):
    """
    Funcion encargada de verificar si el usuario quería poner numeros decimales
    Recorre la lista en busca de un ".", si lo encuentra remplaza los caracteres dentro de la lista
    por un solo caracter
    """
    #Chequeo de punto decimal
    #Variable encargada de recorrer la lista
    detectar = 0
    #Ciclo encargado de recorrer la lista y verificar si hay un punto decimal
    while detectar <= len(lista)-1:
        if lista[detectar] == ".":
            #En caso de encontrar un punto decimal, se crea un nuevo caracter con el numero anterior, el punto y el numero posterior
            caracter = lista[detectar-1] + lista[detectar] + lista[detectar+1]
            lista[detectar-1:detectar+2] = [caracter]
        else:
            #Si no se encuentra un punto decimal, se sigue recorriendo la lista
            detectar += 1

    #Se regresa la lista con los valores decimales ya formados
    return lista

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
    return lista

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
                    #Se realiza la operación de división y se remplaza el contenido de la lista por el resultado
                    resultado = float(lista[movimiento-1]) / float(lista[movimiento+1])
                    #Se remplaza el contenido de la lista por el resultado
                    lista[movimiento-1:movimiento+2] = [resultado]
                    #print(f"division: {lista}")
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
    return lista


print("=======================================")
print("Ejercicio 1 - CALCULADORA\n")
print("=======================================")

print(f"= {calculadora()}")


