import matplotlib.pyplot as plt
import random
import numpy as np


def ingresarCantidad():
    return abs(int(input('Número re repeticiones:')))


def generarLista(cantidad):
    lista = [0] * 37
    for i in range(0, cantidad):
        n = random.randint(0, 36)
        lista[n] += 1
    return lista


def promedio(lista):
    return sum(lista)/len(lista)


# datos
cantidad = ingresarCantidad()
lista = generarLista(cantidad)
# print(lista) #para debug

# frecuencias
plt.stem(lista)
plt.title('Frecuencias Ruleta ('+str(cantidad)+' iteraciones)')
plt.plot(lista, 'ro')
plt.axis([-1, len(lista), 1, max(lista)*1.1])
plt.ylabel('Tiros')
plt.xlabel('Números')
plt.show()
