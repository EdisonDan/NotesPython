#Escribe un programa que incluya una matriz bidimensional
#Matriz 3x3
matriz = [
    [11,12,13],
    [14,15,16],
    [17,18,19]
    ]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j
    return None

#Solicitar buscar un valor
numero_buscar= 19

#Llamo la función

resultado = buscar_valor(matriz, numero_buscar)

if resultado:
    print(f"El valor {numero_buscar} se encuentra en la posición {resultado [1]} {resultado [1]}")
else:
    print(f"El valor {numero_buscar} no se encuentra en la matriz")