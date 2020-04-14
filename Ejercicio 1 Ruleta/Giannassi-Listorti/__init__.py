import matplotlib.pyplot as plt
import numpy as np
import time

calcularTiempo = True
guardar = True
ubicacionGuardado = "graphs/"

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

def tiempoDeMedida():
    return time.perf_counter()

def cargarResultadoGraphs(frecuencies, averages, variances, deviations, save, final=False):
    # Subplots Config
    fig, axs = plt.subplots(2, 2)

    # Title and Names Config
    if final:
        filename="final_"
        message="3er 4-Stack de Gráficos"
        fig.canvas.set_window_title("Análisis 3er Stack: Promedio de Arrays de Resultados (de 0 a "+str(iteraciones)+" tiradas)")
    else:
        filename="simple_"
        message="1er 4-Stack de Gráficos"
        fig.canvas.set_window_title("Análisis 1er Stack: 1 Array de Resultados (de 0 a "+str(iteraciones)+" tiradas)")

    # Set Window Position
    manager = plt.get_current_fig_manager() # Current Window's Manager
    screen_x, screen_y = manager.window.wm_maxsize # Screen Size
    if final:
        coord_x = str(int(screen_x/4))
        coord_y = str(int(screen_y/2))
    else:
        coord_x = ("0")
        coord_y = ("0")
    manager.window.wm_geometry("+" + coord_x + "+" + coord_y) # Set Values

    # Relative Frecuencies Graph
    axs[0, 0].plot(frecuencies, 'tab:blue', label="FRN")
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(fr_t, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(muestra))

    # Averages Graph
    axs[0, 1].plot(averages, 'tab:orange', label="VPN")
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(pr_t, color='red', linestyle='--', label="VPE")

    # Variances Graph
    axs[1, 0].plot(variances, 'tab:green', label="VVN")
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_t, color='red', linestyle='--', label="VVE")

    # Deviations Graph
    axs[1, 1].plot(deviations, 'tab:purple', label="VDN")
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(desv_t, color='red', linestyle='--', label="VDE")
    
    # Details Config
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()
    
    # Save Plot (PNG Image)
    if save:
        try:
            plt.savefig(ubicacionGuardado + filename + "graph_iterations_" + str(iteraciones) + ".png")
            print(message + " Guardado Correctamente")
        except:
            print(message + " NO fue guardado porque hubo un problema")
        print()

# Load (for Plotting) Every Array of Results Simultaneously
# Graphs Loaded: Relative Frecuency, Mean, Variance, Deviation (4-Graph Stack)
def cargarTodosResultadosGraphs(frecuencies, averages, variances, deviations, save):
    # Subplots Config
    fig, axs = plt.subplots(2, 2)

    # Title Config
    fig.canvas.set_window_title("Análisis 2do Stack: Todos los Arrays de Resultados (de 0 a "+str(iteraciones)+" tiradas)")

    # Set Window Position
    manager = plt.get_current_fig_manager() # Current Window's Manager
    screen_x, screen_y = manager.window.wm_maxsize() # Screen Size
    coord_x = str(int(screen_x/2))
    coord_y = "0"
    manager.window.wm_geometry("+" + coord_x + "+" + coord_y) # Set Values

    # Relative Frecuencies Graph
    axs[0, 0].plot(frecuencies[0], 'tab:blue')
    axs[0, 0].plot(frecuencies[1], 'tab:orange')
    axs[0, 0].plot(frecuencies[2], 'tab:green')
    axs[0, 0].plot(frecuencies[3], 'tab:purple')
    axs[0, 0].plot(frecuencies[4], 'tab:pink')
    axs[0, 0].plot(frecuencies[5], 'tab:brown')
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(fr_t, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(muestra))

    # Averages Graph
    axs[0, 1].plot(averages[0], 'tab:blue')
    axs[0, 1].plot(averages[1], 'tab:orange')
    axs[0, 1].plot(averages[2], 'tab:green')
    axs[0, 1].plot(averages[3], 'tab:purple')
    axs[0, 1].plot(averages[4], 'tab:pink')
    axs[0, 1].plot(averages[5], 'tab:brown')
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(pr_t, color='red', linestyle='--', label="VPE")

    # Variances Graph
    axs[1, 0].plot(variances[0], 'tab:blue')
    axs[1, 0].plot(variances[1], 'tab:orange')
    axs[1, 0].plot(variances[2], 'tab:green')
    axs[1, 0].plot(variances[3], 'tab:purple')
    axs[1, 0].plot(variances[4], 'tab:pink')
    axs[1, 0].plot(variances[5], 'tab:brown')
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_t, color='red', linestyle='--', label="VVE")

    # Deviations Graph
    axs[1, 1].plot(deviations[0], 'tab:blue')
    axs[1, 1].plot(deviations[1], 'tab:orange')
    axs[1, 1].plot(deviations[2], 'tab:green')
    axs[1, 1].plot(deviations[3], 'tab:purple')
    axs[1, 1].plot(deviations[4], 'tab:pink')
    axs[1, 1].plot(deviations[5], 'tab:brown')
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(desv_t, color='red', linestyle='--', label="VDE")
    
    # Details Config
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()

    # Save Plot (PNG Image)
    if save:
        try:
            plt.savefig(ubicacionGuardado + "multi_graph_iterations_" + str(iteraciones) + ".png")
            print("2do 4-Stack de Gráficos Guardado Correctamente")
        except:
            print("2do 4-Stack de Gráficos NO fue guardado porque hubo un problema")
        print()


if __name__ == "__main__":

    numeros = np.arange(0, 37)

    # print(numeros)

    fr_t = round(1/len(numeros), 6)
    pr_t = round(calcularPromedio(numeros), 6) 
    var_t = round(calcularVarianza(numeros), 6) 
    desv_t = round(calcularDesviacionDesdeVarianza(var_t), 6)


    print("Frecuencia Relativa Esperada: "+str(fr_t))
    print("Valor Promedio Esperado: "+str(pr_t))
    print("Varianza Esperada: "+str(var_t))
    print("Desvío Esperado: "+str(desv_t))

    # Total "Results" to Plot at the Same Time (For the 2nd 4-Stack of Graphs):
    # Recommended: Between 5 and 10
    resultados = 6

    # Total Iterations (Example: Try with 500)
    iteraciones = 0
    while (iteraciones==0):
        # Validation
        iteraciones = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
    print()

    muestra = -1
    while (muestra>36 or muestra<0):
        # Validation
        muestra = abs(int(float(input("Ingrese su Número (Entre 0 y 36): "))))
    print()

    # Timer (Execution Time Measurement)
    tiempoInicial = tiempoDeMedida()

    # For Every Iteration: Mean-Deviaton-Variance Values & Relative Frecuency of One Number
    # Matix Re-Size: Arrays of Arrays, Needed for the Graph with few "Results" simultaniously
    fr_array = np.zeros((resultados, iteraciones+1)) # Relative Frecuencies of One Number Array Initialization
    pr_array = np.zeros((resultados, iteraciones+1)) # Average (Mean) Arry Initialization
    var_array = np.zeros((resultados, iteraciones+1)) # Variance Array Initialization
    desv_array = np.zeros((resultados, iteraciones+1)) # Deviation Array Initialization
    valores_ruleta = np.zeros(37, dtype=int) # Initialization for Obtained Roulette's Values
    print("Cargando "+str(iteraciones)+" iteraciones...")
    tiempoCargaAcumulado = 0 # Variable Needed for Time Measurement


    for i in range(resultados):
        for n in range(1, iteraciones+1):
            # Playing Roulette and Analyzing the Obtained Numbers
            valores_ruleta = np.random.randint(0, 37, n) # Random Numbers Generator (Total = N Numbers)
            # Occurrences Counter of One_Number (The Input Number)
            ocurrencias_muestra = np.count_nonzero(valores_ruleta == muestra)
            # Filling Important Arrays (In the Matrix Position for the Actual Results Array)
            fr_array[i][n] = ocurrencias_muestra / n                            # Relative Frecuency of "One_Number"
            pr_array[i][n] = round(calcularPromedio(valores_ruleta), 6)                  # Average (Mean)
            var_array[i][n] = varianza = round(calcularVarianza(valores_ruleta), 6)   # Variance
            desv_array[i][n] = round(calcularDesviacionDesdeVarianza(varianza), 6)      # Standard Deviation (Squa
        
      # Feedback: Calculate and Show intermediate processing Time
        if calcularTiempo:
            ultimoTiempoCarga = tiempoDeMedida() - tiempoInicial - tiempoCargaAcumulado
            tiempoCargaAcumulado = tiempoDeMedida() - tiempoInicial
            print("Array Resultado " + str(i+1) + " de "+str(resultados) + " completado en " + str(round(ultimoTiempoCarga, 6)) + " segundos")
        else:
            print("Array Resultado " + str(i+1) + " de "+str(resultados) + " completado")

        # Total Calculation Time
    if calcularTiempo:
        tiempoFinal = round(tiempoDeMedida() - tiempoInicial, 6)
        print("Todos los Arrays de Resultados fueron completados en " + str(tiempoFinal) + " segundos")
    else:
        print("Todos los Arrays de Resultados fueron completados")
    print()

    # PLOTTING

    # First Array of Results' Graphs
    cargarResultadoGraphs(fr_array[0], pr_array[0], var_array[0], desv_array[0], guardar)
    
    # Now, Comparing all the Results Array at the same Time
    cargarTodosResultadosGraphs(fr_array, pr_array, var_array, desv_array, guardar)

    # New Result Array with the Average of all Results Arrays
    final_rfr_array = (fr_array[0] + fr_array[1] + fr_array[2] + fr_array[3] + fr_array[4] + fr_array[5]) / resultados
    final_avg_array = (pr_array[0] + pr_array[1] + pr_array[2] + pr_array[3] + pr_array[4] + pr_array[5]) / resultados
    final_var_array = (var_array[0] + var_array[1] + var_array[2] + var_array[3] + var_array[4] + var_array[5]) / resultados
    final_dev_array = (desv_array[0] + desv_array[1] + desv_array[2] + desv_array[3] + desv_array[4] + desv_array[5]) / resultados

    cargarResultadoGraphs(final_rfr_array, final_avg_array, final_var_array, final_dev_array, guardar, final=True)

    # Plotting all the Graphs
    plt.show()