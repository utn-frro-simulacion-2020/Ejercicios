import random as random
import numpy as np
import matplotlib.pyplot as plt

def generarTiradaRuleta():
    return random.randint(0,36)
     
def iteracionDeTiradas(cantidadDeTiradas):
    valores = []
    for _ in range(0,cantidadDeTiradas):
        valores.append(generarTiradaRuleta())
    return valores

def frecuenciasRelativasCalculo(lista):
    return lista.count(random.randint(0,36)) / len(lista)
        
def iteracionesTotales(cantMaxTiradas):
    frecuenciasRelativas = []
    promedios = []
    varianzas = []
    desvios = [] 
    for i in range(1,cantMaxTiradas):
        iteracion = iteracionDeTiradas(i)
        promedios.append(np.mean(iteracion))
        varianzas.append(np.var(iteracion))
        desvios.append(np.std(iteracion))
        frecuenciasRelativas.append(frecuenciasRelativasCalculo(iteracion))
    return frecuenciasRelativas, promedios, varianzas, desvios

# Main ------------------------------------------------------------------------------------------

ruleta=[]
for i in range(0,37): ruleta.append(i)

frecuenciaRelativaEsperada = frecuenciasRelativasCalculo(ruleta)
promedioEsperado = np.mean(ruleta)
varianzaEsperado = np.var(ruleta)
desvioEsperado = np.std(ruleta)

z = int(input("Ingrese la cantidad máxima de tiradas a realizar: "))
frecuenciasRelativasGrafico, promediosGrafico, varianzasGrafico, desviosGrafico = iteracionesTotales(z)

# Plot n°1 - Análisis de frecuencia relativa
plt.subplot(2, 2, 1)
plt.title("Frecuencia Relativa")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+frecuenciasRelativasGrafico, 'tab:pink', label='Frecuencia relativa')
plt.axhline(frecuenciaRelativaEsperada, color='black', linestyle='dashed', label='Frecuencia relativa esperada')
plt.xlim(xmin=1)
plt.legend(loc='upper right')

# Plot n°2 - Análisis de promedio
plt.subplot(2, 2, 2)
plt.title("Promedio")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+promediosGrafico, 'tab:purple', label='Promedio')
plt.axhline(promedioEsperado, color='black', linestyle='dashed', label='Promedio esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

# Plot n°3 - Análisis de varianza
plt.subplot(2, 2, 3)
plt.title("Varianza")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+varianzasGrafico, 'tab:blue', label="Varianza")
plt.axhline(varianzaEsperado, color='black', linestyle='dashed', label='Varianza esperada')
plt.xlim(xmin=1)
plt.legend(loc='lower right')


# Plot n°4 - Análisis de desvío
plt.subplot(2, 2, 4)
plt.title("Desvío")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+desviosGrafico, 'tab:orange', label='Desvío')
plt.axhline(desvioEsperado, color='black', linestyle='dashed', label='Desvío esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

plt.show()