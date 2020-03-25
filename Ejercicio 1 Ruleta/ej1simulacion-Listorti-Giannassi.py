import matplotlib.pyplot as plt
import random

def generarLista(cantidad):
    lista = []
    for i in range(0,cantidad): #de 10 para ver si son los mismos num
        lista.append(random.randint(0,36))
    return lista


def promedio(lista):
    return sum(lista)/len(lista)


lista = generarLista(10000)
plt.plot(lista, 'ro')
plt.ylabel('some numbers')
plt.show()
print(lista)

# the histogram of the data
n, bins, patches = plt.hist(lista, 50, density=1, facecolor='g', alpha=0.75)

#qué hacemos? esperamos la consigna?
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, 'mu='+ str(promedio(lista)))
#plt.axis([40, 160, 0, 0.03]) #se ve piolita?
plt.grid(True)
plt.show() 

#ahora habria que sacar media y moda ahi