import matplotlib.pyplot as plt
import random as rand
import numpy as np

def ingresarCantidad():
    return abs(int(input('Repeticiones:')))

if __name__ == "__main__":

    numeros = np.arange(0, 37)

    #print(numeros)

    fr_t = round(1/len(numeros),2)
    med_t = round(np.mean(numeros),2)
    desv_t = round(np.std(numeros),2)
    var_t = round(np.var(numeros),2)

    #print(str(fr_t)+" "+str(med_t)+" "+str(desv_t)+" "+str(var_t))
    
    muestra = rand.randint(0, 37)

    #Inicialización de arrays
    fr_array = [0]
    med_array = [0]
    desv_array = [0]
    var_array = [0]

    iteraciones = ingresarCantidad()
    for i in range (1, iteraciones):
        