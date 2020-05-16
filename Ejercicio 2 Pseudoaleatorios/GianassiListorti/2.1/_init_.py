import numpy as np
from terminaltables import AsciiTable
from generadores import GeneradorGCL
from generadores import GeneradorMiddleSquare
from tests import *
from os import system, name

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def muestraNumpy(n, seed):
    np.random.seed(seed)
    array = np.zeros(n)
    for i in range(n):
        array[i] = np.random.random()
    return array

def testear(muestra, tipo):
    table_data = [
        ['Test '+tipo, 'Resultado']
    ]
    print("Realizando tests para la muestra generada por "+tipo)
    print("Test de Kolmogorov Smirnov: ")
    result = kstest(muestra)
    table_data.append(["Kolmogorov Smirnov", result])
    print("Test de Chi Cuadrado: ")
    result = chiCuadrado(muestra)
    table_data.append(["Chi Cuadrado", result])
    print("Test de Corridas MediaArriba y Abajo de la Media:")
    result = corridasArribaAbajoMediaTest(muestra)
    table_data.append(["Corridas Arriba y Abajo de la Media", result])

    table = AsciiTable(table_data)
    print(table.table)

if __name__ == "__main__":
    clearScreen()
    print("BIENVENIDO A LA SIMULACIÓN DE NÚMEROS PSEUDOALEATORIOS.")
    seed = int(float(input("Ingrese una semilla: ")))
    #Numpy
    muestra = muestraNumpy(1000, seed)
    testear(muestra, "Numpy")
    #GCL
    muestra =  GeneradorGCL(seed).muestra(1000)
    testear(muestra, "Generador GCL")
    #Middle-Square
    muestra = GeneradorMiddleSquare(seed).muestra(1000)
    testear(muestra, "Generador Middle Square")
