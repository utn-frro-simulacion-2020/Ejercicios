import random as random
import numpy as np
import matplotlib.pyplot as plt

def generarTiradaRuleta():
    return random.randint(0,36)
     
def iteraciondeTiradas(cantidadDeTiradas):
    valores = []
    for i in range(0,cantidadDeTiradas):
        valores.append(generarTiradaRuleta())
    return valores

def frecuenciasRelativasCalculo(lista):
    nRandom = random.randint(0,36)
    frecuenciaAbsoluta = lista.count(nRandom)
    frecuenciaRelativa = frecuenciaAbsoluta / len(lista)
    return frecuenciaRelativa
        
def iteracionesTotales(cantMaxTiradas):
    frecuenciasRelativas = []
    promedios = []
    varianzas = []
    desvios = [] 
    for i in range(1,cantMaxTiradas):
        promedios.append(np.mean(iteraciondeTiradas(i)))
        varianzas.append(np.var(iteraciondeTiradas(i)))
        desvios.append(np.std(iteraciondeTiradas(i)))
        frecuenciasRelativas.append(frecuenciasRelativasCalculo(iteraciondeTiradas(i)))
    return frecuenciasRelativas, promedios, varianzas, desvios

# Main ------------------------------------------------------------------------------------------

ruleta=[]
for i in range(0,36): ruleta.append(i)

frecuenciaRelativaEsperada = frecuenciasRelativasCalculo(ruleta)
promedioEsperado = np.mean(ruleta)
varianzaEsperado = np.var(ruleta)
desvioEsperado = np.std(ruleta)

z = int(input("Ingrese la cantidad máxima de tiradas a realizar: "))
frecuenciasRelativasGrafico, promediosGrafico, varianzasGrafico, desviosGrafico = iteracionesTotales(z)

# Plot n°1 - Análisis de Frecuencia Relativa
plt.title("Frecuencia Relativa del Nro X")
plt.xlabel("Nro de tiradas")
plt.grid(True)
plt.plot([0]+frecuenciasRelativasGrafico)
plt.axhline(frecuenciaRelativaEsperada, color='r', linestyle='dashed')
plt.xlim(xmin=1)
plt.show()

# Plot n°2 - Análisis de promedio
plt.title("Promedio")
plt.xlabel("Nro de Tiradas")
plt.grid(True)
plt.plot([0]+promediosGrafico)
plt.axhline(promedioEsperado, color='r', linestyle='dashed')
plt.xlim(xmin=1)
plt.show()

# Plot n°3 - Análisis de varianzas
plt.title("Varianza")
plt.xlabel("Nro de tiradas")
plt.grid(True)
plt.plot([0]+varianzasGrafico)
plt.axhline(varianzaEsperado, color='r', linestyle='dashed')
plt.xlim(xmin=1)
plt.show()

# Plot n°4 - Análisis de Desvios
plt.title("Desvío")
plt.xlabel("Nro de tiradas")
plt.grid(True)
plt.plot([0]+desviosGrafico)
plt.axhline(desvioEsperado, color='r', linestyle='dashed')
plt.xlim(xmin=1)
plt.show()