from os import system, name
from estrategias import *
from graficador import graficarResultados

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():

    capitalFinito = True
    capitalDisponible = 1000
    jugadasMax = 50000
    simulaciones = 5

    clearScreen()

    while True:
        print("===================================")
        print("¡Bienvenido al simulador de ruleta!")
        print("===================================")
        print("")

        if capitalFinito: print("Capital disponible: $" + str(capitalDisponible))
        else: print("Capital disponible: ∞")
        print("Jugadas máximas a realizar: " + str(jugadasMax))
        print("Simulaciones simultáneas a realizar: " + str(simulaciones))
        print("")

        print("Por favor, seleccione la opción:")
        print("     1 _ Modificar preferencias")
        print("     2 _ Simular Martingale")
        print("     3 _ Simular Martingale Modificado")
        print("     4 _ Simular Martingale Inverso")
        print("     5 _ Simular Fibonacci")
        print("     6 _ Simular Proporción Constante")
        print("     7 _ No jugar")
        print("     8 _ Salir")
        print("")

        opt = int(input("--> "))

        resultados = []

        if opt == 1:
            clearScreen()
            print("===================================")
            print("============ Opciones =============")
            print("===================================")
            print("")
            capitalFinito = True if input("Desea invertir con capital finito? (s/n) --> ") == "s" else False
            capitalDisponible = 0 if not capitalFinito else int(input("Ingrese el capital disponible --> $"))
            jugadasMax = int(input("Ingrese la cantidad de jugadas máximas a realizar --> "))
            simulaciones = int(input("Ingrese la cantidad de simulaciones simultáneas a realizar --> "))

        elif opt == 2:
            for i in range(0,simulaciones):
                resultados.append(estrategiaMartingale(capitalDisponible, "p", 0, jugadasMax))
            graficarResultados(resultados)

        elif opt == 3:
            aumento = int(input("Ingrese el valor monetario extra a añadir en cada apuesta perdedora --> $"))
            for i in range(0,simulaciones):
                resultados.append(estrategiaMartingale(capitalDisponible, "p", aumento, jugadasMax))
            graficarResultados(resultados)

        elif opt == 4:
            for i in range(0,simulaciones):
                resultados.append(estrategiaMartingaleInverso(capitalDisponible, "p", jugadasMax))
            graficarResultados(resultados)

        elif opt == 5:
            for i in range(0,simulaciones):
                resultados.append(estrategiaFibonacci(capitalDisponible, "p", jugadasMax))
            graficarResultados(resultados)

        elif opt == 6:
            if capitalFinito:
                proporcion = int(input("Ingrese la proporción de la caja a apostar en cada apuesta --> %"))
                for i in range(0,simulaciones):
                    resultados.append(estrategiaPropConstante(capitalDisponible, proporcion, "p", jugadasMax))
                graficarResultados(resultados)
            else:
                clearScreen()
                print("Esta estrategia no admite dinero ilimitado.")
                input("Presione Enter para continuar...")

        elif opt == 7:
            clearScreen()
            print("Felicitaciones, no ha jugado a la ruleta y  ha conservado todo su dinero.")
            input("Presione Enter para continuar...")

        elif opt == 8:
            break

        clearScreen()

menu()
