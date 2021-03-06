import matplotlib.pyplot as plt
from os import system, name
import numpy as np
from graficador import graficarResultados
from estrategias import *

def configuraciones():

    iteraciones = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
    while (iteraciones<=0):
        print("Cantidad de iteraciones incorrecta (tiene que hacer por lo menos una iteración)")
        iteraciones = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
        
    capital_inicial = abs(float(input("Ingrese capital inicial (0 para infinito): "))) 
    while (capital_inicial<0):
        print("Cantidad de capital incorrecta")
        capital_inicial = abs(float(input("Ingrese capital inicial (0 para infinito): ")))

    paridad = input("Elige por Par o Impar (p/i): ")
    while (paridad!="p" and paridad!="i"):
        print("Tiene que elegir entre par(p) e impar(i)")
        paridad = abs(int(float(input("Elige por Par o Impar (p/i): "))))

    return capital_inicial, paridad, iteraciones

def menu():
    opcion = -1
    corridas = 6
    while(opcion!=0):
        print("Estrategias:")
        print("1 - Martingala")
        print("2 - D'Alembert")
        print("3 - Fibonacci")
        print("0 - Salir")
        opcion= abs(int(float(input("Seleccione una estrategia: "))))
        while (opcion<0 and opcion>3):
            print("Opción incorrecta")
            opcion= abs(int(float(input("Seleccione una estrategia: "))))
        paridad = ""
        iteraciones = 0
        capital_inicial = 0
        apuesta_inicial = 0
        resultados = []
        if(opcion!=0):
            capital_inicial, paridad ,iteraciones = configuraciones()
        if opcion==1:
            apuesta_inicial = abs(int(float(input("Ingrese apuesta inicial (tiene que ser menor o igual al capital inicial, si es capital infinito puede ser cualquier numero positivo): "))))
            if(capital_inicial==0):
                while(apuesta_inicial<0):
                    print("Cantidad de apuesta incorrecta")
                    apuesta_inicial = abs(float(input("Ingrese apuesta inicial (tiene que ser menor o igual al capital inicial, si es capital infinito puede ser cualquier numero positivo): ")))
            else:
                while(apuesta_inicial>capital_inicial):
                    print("Cantidad de apuesta incorrecta")
                    apuesta_inicial = abs(float(input("Ingrese apuesta inicial (tiene que ser menor o igual al capital inicial, si es capital infinito puede ser cualquier numero positivo): ")))
            for i in range(0,corridas):
                resultados.append(Martingala(capital_inicial, paridad, apuesta_inicial, iteraciones))
            graficarResultados(resultados,1)
            graficarResultados(resultados,corridas)
        elif opcion==2:
            for i in range(0,corridas):
                resultados.append(Dalembert(capital_inicial, paridad, 1, iteraciones))
            graficarResultados(resultados,1)
            graficarResultados(resultados,corridas)
        elif opcion==3:
            for i in range(0,corridas):
                resultados.append(Fibonacci(capital_inicial, paridad, 1, iteraciones))
            graficarResultados(resultados,1)
            graficarResultados(resultados,corridas)

    return None

if __name__ == "__main__":

    menu()
  
