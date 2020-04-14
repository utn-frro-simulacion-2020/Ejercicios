import matplotlib.pyplot as plt
import numpy as np

def ingresarCantidad():
    return abs(int(input('Repeticiones:')))

def calcularPromedio(numeros):
    return np.mean(numeros)

def calcularVarianza(numeros):
    return np.var(numeros)

def calcularDesviacion(numeros):
    return np.std(numeros)

def calcularDesviacionDesdeVarianza(numeros):
    return (numeros ** 0.5)

def cargarResultadoGraphs(frecuencias, promedios, varianzas, desvios, final):
    # Configuración de subplots
    fig, axs = plt.subplots(2, 2)

    if final:
        plt.title("Resultados con una corrida")
    else:
        plt.title("Resultados con 5 corridas")

    # Gráfico de frecuencias relativas
    axs[0, 0].plot(frecuencias, 'tab:blue', label="FRN")
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(fr_t, color='red', linestyle='--', label="FRT")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(muestra))

    # Gráfico de promedios
    axs[0, 1].plot(promedios, 'tab:orange', label="VPN")
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(pr_t, color='red', linestyle='--', label="VPT")

    # Gráfico de varianzas
    axs[1, 0].plot(varianzas, 'tab:green', label="VVN")
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_t, color='red', linestyle='--', label="VVT")

    # Gráfico de desvíos
    axs[1, 1].plot(desvios, 'tab:purple', label="VDN")
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(desv_t, color='red', linestyle='--', label="VDT")
    
    # Detalles de configuración
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()


if __name__ == "__main__":

    numeros = np.arange(0, 37)

    fr_t = round(1/len(numeros), 6)
    pr_t = round(calcularPromedio(numeros), 6) 
    var_t = round(calcularVarianza(numeros), 6) 
    desv_t = round(calcularDesviacionDesdeVarianza(var_t), 6)


    print("Frecuencia Relativa Esperada: "+str(fr_t))
    print("Valor Promedio Esperado: "+str(pr_t))
    print("Varianza Esperada: "+str(var_t))
    print("Desvío Esperado: "+str(desv_t))

    # Resultados totales para trazar al mismo tiempo (para la segunda pila de 4 gráficos):
    # Recomendado: entre 5 y 10
    resultados = 6

    # Iteraciones totales (Ejemplo: probá con 500)
    iteraciones = 0
    while (iteraciones==0):
        # Validación
        iteraciones = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
    print()

    muestra = -1
    while (muestra>36 or muestra<0):
        # Validación
        muestra = abs(int(float(input("Ingrese su Número (Entre 0 y 36): "))))
    print()

    # Para cada iteración: Los valores del promedio, la varianza y el desvío, y la frecuencia relativa de una muestra
    # Cambio de tamaño de matriz: Arreglos de Arreglos, necesarios para el gráfico con pocos resultados simultáneamente
    fr_array = np.zeros((resultados, iteraciones+1)) # Inicialización del array de frecuencia relativa de una muestra
    pr_array = np.zeros((resultados, iteraciones+1)) # Inicialización del array de promedios
    var_array = np.zeros((resultados, iteraciones+1)) # Inicialización del array de varianzas
    desv_array = np.zeros((resultados, iteraciones+1)) # Inicialización del array de desvíos
    valores_ruleta = np.zeros(37, dtype=int) # Inicialización para los valores obtenidos de la ruleta
    print("Cargando "+str(iteraciones)+" iteraciones...")


    for i in range(resultados):
        for n in range(1, iteraciones+1):
            # Jugando a la ruleta y analizando los números obtenidos
            valores_ruleta = np.random.randint(0, 37, n) # Generador de números aleatorios (Total = N números)
            # Contador de ocurrencias de la muestra (El número ingresado)
            ocurrencias_muestra = np.count_nonzero(valores_ruleta == muestra)
            # llenado de arreglos importantes (en la posición de matriz para el arreglo de resultados reales)
            fr_array[i][n] = ocurrencias_muestra / n                            # Frecuencia relativa de la muestra
            pr_array[i][n] = round(calcularPromedio(valores_ruleta), 6)               # Promedio
            var_array[i][n] = varianza = round(calcularVarianza(valores_ruleta), 6)   # Varianza
            desv_array[i][n] = round(calcularDesviacionDesdeVarianza(varianza), 6)    # Desviación estándar

    # Trazado de Gráficos

    # Primer array de resultados
    cargarResultadoGraphs(fr_array[0], pr_array[0], var_array[0], desv_array[0], False)

    # Nuevo array de resultados con el promedio de todos los arrays de resultados
    fr_array_final = (fr_array[0] + fr_array[1] + fr_array[2] + fr_array[3] + fr_array[4] + fr_array[5]) / resultados
    pr_array_final = (pr_array[0] + pr_array[1] + pr_array[2] + pr_array[3] + pr_array[4] + pr_array[5]) / resultados
    var_array_final = (var_array[0] + var_array[1] + var_array[2] + var_array[3] + var_array[4] + var_array[5]) / resultados
    desv_array_final = (desv_array[0] + desv_array[1] + desv_array[2] + desv_array[3] + desv_array[4] + desv_array[5]) / resultados

    # Último array de resultados
    cargarResultadoGraphs(fr_array_final, pr_array_final, var_array_final, desv_array_final, True)

    # Trazando todas las gráficas
    plt.show()