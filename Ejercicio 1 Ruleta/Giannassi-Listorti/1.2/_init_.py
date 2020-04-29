import matplotlib.pyplot as plt
import numpy as np

def girarRuleta():
    return np.random.randint(0,36)

def getColor(numero):
    return colores[numero]    

def getParidad(numero):
    if(numero%2)==0:
        return "par"
    else:
        return "impar"

def getFila(numero):
    fila1 = [1,4,7,10,13,16,19,22,25,28,31,34]
    fila2 = [2,5,8,11,14,17,20,23,26,29,32,35]
    fila3 = [3,6,9,12,15,18,21,24,27,30,33,36]
    if(numero in fila1):
        return 1
    elif(numero in fila2):
        return 2
    elif(numero in fila3):
        return 3
    

def martinGala(iteraciones, capital_inicial):
    print("Martingala se usa en apuestas simples (1-par 2-impar 3-rojo 4-negro 5-fila1 6-fila2 7-fila3).")
    opcion = abs(int(float(input("Ingrese opción: ")))) 
    capital = capital_inicial
    apuestaInicial=-1
    while(apuestaInicial<=0 or (capital_inicial!=0 and apuestaInicial>capital)):
        apuestaInicial = abs(float(input("Ingrese apuesta inicial: ")))
    apuesta = apuestaInicial
    capital_array = np.zeros((resultados, iteraciones+1))
    victorias_array = np.zeros((resultados, iteraciones+1))
    for j in range(resultados):
        for i in range(0,iteraciones):
            if(capital_inicial==0 or capital>=apuesta):
                gano = False
                num = girarRuleta()
                if(opcion==1 and getParidad(num)=="par") or (opcion==2 and getParidad(num)=="impar") or (opcion==3 and getColor(num)=="rojo") or (opcion==4 and getColor(num)=="negro") or (opcion==5 and getFila(num)==1) or (opcion==6 and getFila(num)==2) or (opcion==7 and getFila(num)==3):
                    gano=True
                    victorias_array[j][i] = victorias_array[j][i] + 1
                if(gano):
                    capital = capital + apuesta
                    apuesta = apuestaInicial
                else:
                    capital = capital - apuesta
                    apuesta = apuesta * 2
            capital_array[j][i] = capital
    return capital_array, victorias_array
    

def dalambert(iteraciones, capital_inicial):
    
    return None

def fibonacci(iteraciones, capital_inicial):
    
    return None

def cargarResultadoGraphs(frecuencias, final):
    fig, axs = plt.subplots(2, 2)

    if final:
        fig.canvas.set_window_title("Resultados con 6 corridas")
    else:
        fig.canvas.set_window_title("Resultados con 1 corrida")

    axs[0, 0].plot(frecuencias, 'tab:blue', label="FRN")
    axs[0, 0].set_title("Frecuencia Relativa")
    plt.setp(axs[0, 0], ylabel="FR del Número ")
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()


if __name__ == "__main__":

    numeros = np.arange(0, 37)
    colores = [None] * 37
    for i in range(0, len(numeros)):
        if numeros[i]==0:
            colores[i] = "verde"
        else:
            if colores[i-1] == "verde" or colores[i-1]== "negro":
                colores[i] = "rojo"
            else:
                colores[i] = "negro"

    resultados = 6

    iteraciones = 0
    while (iteraciones==0):
        iteraciones = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
        
    capital_inicial = -1  
    while (capital_inicial<0):
        capital_inicial = abs(float(input("Ingrese capital inicial (0 para infinito): ")))
    
    print("Estrategias:")
    print("1 - Martingala")
    print("2 - D'Alambert")
    print("3 - Fibonacci")
    opcion = 0
    while (opcion==0):
        opcion= abs(int(float(input("Seleccione una estrategia: "))))

    if opcion==1:
        capital_array, victorias_array = martinGala(iteraciones, capital_inicial)
    elif opcion==2:
        dalambert(iteraciones, capital_inicial)
    elif opcion==3:
        fibonacci(iteraciones, capital_inicial)  

    cargarResultadoGraphs(victorias_array ,False)

    #fr_array_final = (fr_array[0] + fr_array[1] + fr_array[2] + fr_array[3] + fr_array[4] + fr_array[5]) / resultados 

    #cargarResultadoGraphs(fr_array_final, True)

    plt.show()