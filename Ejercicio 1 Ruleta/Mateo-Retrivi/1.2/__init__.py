from os import system, name
from estrategias import *
from graficador import graficarResultado

def clearScreen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def menu():
    capitalFinito = True
    capitalDisponible = 1000
    clearScreen()
    while True:
        print("===================================")
        print("¡Bienvenido al simulador de ruleta!")
        print("===================================")
        print("")

        if capitalFinito: print("Capital Disponible: $" + str(capitalDisponible))
        else: print("Capital Disponible: Infinito")
        print("")

        print("Por favor, seleccione la opción:")
        print("     1 _ modificar preferencias")
        print("     2 _ Simular Martingale")
        print("     3 _ Simular Fibonacci")
        print("     4 _ Simular Otra cosa")
        print("     5 _ No jugar")
        print("     6 _ Salir")
        print("")

        opt = int(input("--> "))
        resultado = ""
        
        if opt == 1:
            clearScreen()
            print("===================================")
            print("============ Opciones =============")
            print("===================================")
            print("")
            capitalFinito = True if input("Desea invertir con capital finito? (s/n) --> ") == "s" else False
            capitalDisponible = 0 if not capitalFinito else int(input("Ingrese el capital disponible --> $")) 

        elif opt == 2:
            graficarResultado(capitalDisponible, estrategiaMartingale(capitalDisponible))

        elif opt == 3:
            graficarResultado(capitalDisponible, estrategiaFibonacci(capitalDisponible, "p"))

        elif opt == 4: 
            graficarResultado(capitalDisponible, estrategiaFibonacci(capitalDisponible, "p"))

        elif opt == 5: 
            clearScreen()
            print("Felicitaciones, no ha jugado a la ruleta y  ha conservado todo su dinero.")
            input("Presione Enter para continuar...")

        elif opt == 6: 
            break
        
        clearScreen()

menu()