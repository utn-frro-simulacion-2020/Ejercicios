import matplotlib.pyplot as plt
import random
import numpy as np


def ingresarCantidad():
    return abs(int(input('Repeticiones:')))


numeros = np.arange(0, 37)

fr_t = round(1/len(numeros),2)
med_t = round(np.mean(numeros),2)
desv_t = round(np.std(numeros),2)
var_t = round(np.var(numeros),2)

print(str(fr_t)+" "+str(med_t)+" "+str(desv_t)+" "+str(var_t))