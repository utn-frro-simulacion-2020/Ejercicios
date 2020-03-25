import matplotlib.pyplot as plt
import random
import numpy as np


def generarLista(cantidad):
    lista = []
    for i in range(0, cantidad):
        lista.append(random.randint(0, 36))
    return lista


def promedio(lista):
    return sum(lista)/len(lista)


def frecuencias(lista):
    l = []
    for i in range(0,36):
        l.append(lista.count(i))
    return l


#datos
cantidad = 100
lista = generarLista(cantidad)
#puntos
plt.plot(lista, 'ro')
plt.ylabel('Números')
plt.xlabel('Tiros')
plt.show()
print(lista)
print(frecuencias(lista))

#histograma
n, bins, patches = plt.hist(
    lista, cantidad, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Números')
plt.ylabel('Probabilidad')
plt.title('Histograma de la Ruleta')
plt.text(60, .025, 'mu=' + str(promedio(lista)))
plt.grid(True)
plt.show()

#barras
numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
frec = frecuencias(lista)
y_pos = np.arange(len(numeros)) #no me salen los tooltips arriba de la función cuando paso el mouse xD pushea así puedo ver aca

plt.bar(y_pos, frec, align='center', alpha=0.5)
plt.xticks(y_pos, numeros)
plt.ylabel('Tiros')
plt.title('Numeros Ruleta') #ejecuta y pasa cap x2

plt.show() #otro error. lo veo, pera