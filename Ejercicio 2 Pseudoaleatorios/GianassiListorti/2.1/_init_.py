import numpy as np
from generadores import GeneradorGCL
from generadores import GeneradorMiddleSquare
from os import system, name

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def doNumpy(n, seed, rango):
    np.random.seed(seed)
    array = np.zeros(n)
    for i in range(n):
        array[i] = np.random.randint(rango[0], rango[1])
    return array

if __name__ == "__main__":
    clearScreen()
    rango = [1, 120]
    print("BIENVENIDO A LA SIMULACIÓN DE NÚMEROS PSEUDOALEATORIOS.")
    seed = int(float(input("Ingrese una semilla: ")))
    print("A continuación generaremos números aleatorioos con esa semilla, comparando dos métodos con el generador de Numpy")
    #Numpy
    print("Comparando 3 muestras del generador de Numpy con la misma semilla")
    print(doNumpy(5, seed, rango))
    print(doNumpy(5, seed, rango))
    print(doNumpy(5, seed, rango))
    middleSquare = GeneradorMiddleSquare(seed)
    print(middleSquare.muestra(100,(1000,350))

