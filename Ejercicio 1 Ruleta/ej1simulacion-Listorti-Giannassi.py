import matplotlib.pyplot as plt
import random


def generarLista(cantidad):
    lista = []
    for i in range(0, cantidad):
        lista.append(random.randint(0, 36))
    return lista


def promedio(lista):
    return sum(lista)/len(lista)


cantidad = 100
lista = generarLista(cantidad)
plt.plot(lista, 'ro')
plt.ylabel('Números')
plt.xlabel('Tiros')
plt.show()
print(lista)


n, bins, patches = plt.hist(
    lista, cantidad, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Números')
plt.ylabel('Probabilidad')
plt.title('Histograma de la Ruleta')
plt.text(60, .025, 'mu=' + str(promedio(lista)))
plt.grid(True)
plt.show()
