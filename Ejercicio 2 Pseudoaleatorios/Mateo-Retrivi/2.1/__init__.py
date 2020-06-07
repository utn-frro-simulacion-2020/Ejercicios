from generators import *
from ourGeneratorFromReddit import randomNumberGenerator, getDataSet
from tests import *
from utils import clearScreen


def menu():

    clearScreen()

    while True:
        print("=====================================================================")
        print("---------- ¡Bienvenido al generador de números aleatorios! ----------")
        print("=====================================================================")
        print("")
        print("- Por favor, seleccione la opción:")
        print("")
        print("  Generar números aleatorios a partir de:")
        print("")
        print("    1 _ Generador GCL")
        print("    2 _ Generador Middle Square")
        print("    3 _ Generador 'From Reddit'")
        print("    4 _ Librería 'Random' de Python")
        print("")
        print("  5 _ Salir")
        print("")

        opt = int(input("--> "))


        if opt == 1:
            while True:
                clearScreen()
                ok = True
                modulus = int(input("Ingrese módulo mayor a 0 --> "))
                multiplier = int(input("Ingrese multiplicador mayor a 0 y menor al módulo --> "))
                increment = int(input("Ingrese incremento mayor o igual a 0 y menor igual al módulo --> "))
                seed = int(input("Ingrese la semilla mayor o igual a 0 y menor al módulo con la cual generar la serie de números random --> "))
                nReturn = int(input("Ingrese la cantidad de números random a generar con la misma semilla --> "))
                clearScreen()

                if not (modulus > 0):
                    print("Ingrese un módulo mayor a 0")
                    ok = False
                if not (multiplier > 0 and multiplier < modulus):
                    print("Ingrese un multiplicador mayor a 0 y menor al módulo")
                    ok = False
                if not (increment >= 0 and increment < modulus):
                    print("Ingrese un incremento mayor o igual a 0 y menor al módulo")
                    ok = False
                if not (seed >= 0 and seed < modulus):
                    print("Ingrese una semilla  mayor o igual a 0 y menor al módulo")
                    ok = False
                if ok: break
                else: input("Presione Enter para continuar...")

            runAllTests(linealCongruentialGenerator(seed, modulus, increment, multiplier, nReturn), "LCG Generator")


        elif opt == 2:
            while True:
                clearScreen()
                ok = True
                seed = int(input("Ingrese la semilla de cantidad de dígitos par con la cual generar la serie de números random --> "))
                nReturn = int(input("Ingrese la cantidad de números random a generar con la misma semilla --> "))
                clearScreen()

                if not (len(str(seed)) % 2 == 0):
                    print("La semilla debe contener un número de dígitos pares")
                    ok = False
                if ok: break
                else: input("Presione Enter para continuar...")

            runAllTests(middleSquareGenerator(seed, nReturn), "Middle Square Generator")


        elif opt == 3:
            clearScreen()
            print("- Por favor, seleccione la opción:")
            print("    1 _ Generador nuevos números random a partir del generador")
            print("    2 _ Visualizar los resultados a partir de numeros ya generados")
            o = int(input("--> "))

            if o == 1:
                clearScreen()
                nReturn = int(input("Ingrese la cantidad de números random a generar --> "))
                randomNumberGenerator(nReturn)

            elif o == 2:
                runAllTests(getDataSet(), "'From Reddit' Generator")

        elif opt == 4:
            clearScreen()
            nReturn = int(input("Ingrese la cantidad de números random a generar --> "))
            runAllTests(pythonRandom(nReturn), "Python 'Random'")

        elif opt == 5: break

        clearScreen()

menu()
