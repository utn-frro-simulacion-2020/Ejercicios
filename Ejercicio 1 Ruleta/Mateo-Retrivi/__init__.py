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

def variasCorridas(cantCorridas, cantMaxTiradas):
    corridas = []
    for _ in range(0,cantCorridas):
        fr, p, v, d = iteracionesTotales(cantMaxTiradas)
        corrida = {'frecuenciasRelativas' : fr, 'promedios' : p, 'varianzas' : v, 'desvios' : d}
        corridas.append(corrida)
    return corridas

# ---------------------------------------- Main --------------------------------------------

ruleta=[]
for i in range(0,37): ruleta.append(i)

frecuenciaRelativaEsperada = frecuenciasRelativasCalculo(ruleta)
promedioEsperado = np.mean(ruleta)
varianzaEsperado = np.var(ruleta)
desvioEsperado = np.std(ruleta)

cantMaxTiradas = int(input("Ingrese la cantidad máxima de tiradas a realizar: "))
cantCorridas = int(input("Ingrese cantidad de corridas del experimento: "))

# ------------------------------------------------------------------------------------------

frecuenciasRelativasGrafico, promediosGrafico, varianzasGrafico, desviosGrafico = iteracionesTotales(cantMaxTiradas)

# Plot n°1 - Análisis de frecuencia relativa
plt.subplot(2, 2, 1)
plt.title("Frecuencia relativa")
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

# ------------------------------------------------------------------------------------------

corridas = variasCorridas(cantCorridas,cantMaxTiradas)

# Plot n°1 - Análisis de frecuencia relativa
plt.subplot(2, 2, 1)
plt.title("Frecuencia relativa de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
for c in corridas:
    plt.plot([0]+c['frecuenciasRelativas'])
plt.axhline(frecuenciaRelativaEsperada, color='black', linestyle='dashed', label='Frecuencia relativa esperada')
plt.xlim(xmin=1)
plt.legend(loc='upper right')

# Plot n°2 - Análisis de promedio
plt.subplot(2, 2, 2)
plt.title("Promedio de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
for c in corridas:
    plt.plot([0]+c['promedios'])
plt.axhline(promedioEsperado, color='black', linestyle='dashed', label='Promedio esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

# Plot n°3 - Análisis de varianza
plt.subplot(2, 2, 3)
plt.title("Varianza de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
for c in corridas:
    plt.plot([0]+c['varianzas'])
plt.axhline(varianzaEsperado, color='black', linestyle='dashed', label='Varianza esperada')
plt.xlim(xmin=1)
plt.legend(loc='lower right')


# Plot n°4 - Análisis de desvío
plt.subplot(2, 2, 4)
plt.title("Desvío de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
for c in corridas:
    plt.plot([0]+c['desvios'])
plt.axhline(desvioEsperado, color='black', linestyle='dashed', label='Desvío esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

plt.show()

# ------------------------------------------------------------------------------------------

pfrecuenciasRelativas = []
pPromedios = []
pDesvios = []
pVarianzas = []

dfrecuenciasRelativas = []
dPromedios = []
dDesvios = []
dVarianzas = []

for i in range(0, len(corridas[0]['desvios'])):
    fr = []
    p = []
    d = []
    v = []
    for c in corridas:
        fr.append(c['frecuenciasRelativas'][i])
        p.append(c['promedios'][i])
        d.append(c['desvios'][i])
        v.append(c['varianzas'][i])

    pfrecuenciasRelativas.append(np.mean(fr))
    pPromedios.append(np.mean(p))
    pDesvios.append(np.mean(d))
    pVarianzas.append(np.mean(v))

    dfrecuenciasRelativas.append(np.std(fr))
    dPromedios.append(np.std(p))
    dDesvios.append(np.std(d))
    dVarianzas.append(np.std(v))

# ------------------------------------------------------------------------------------------

plt.subplot(2, 2, 1)
plt.title("Promedio de las frecuencias relativas de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+pfrecuenciasRelativas, 'tab:pink')
plt.axhline(frecuenciaRelativaEsperada, color='black', linestyle='dashed', label='Frecuencia relativa esperada')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

plt.subplot(2, 2, 2)
plt.title("Promedio de los promedios de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+pPromedios, 'tab:purple')
plt.axhline(promedioEsperado, color='black', linestyle='dashed', label='Promedio esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

plt.subplot(2, 2, 3)
plt.title("Promedio de las varianzas de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+pVarianzas, 'tab:blue')
plt.axhline(varianzaEsperado, color='black', linestyle='dashed', label='Varianza esperada')
plt.xlim(xmin=1)
plt.legend(loc='lower right')


plt.subplot(2, 2, 4)
plt.title("Promedio de los desviós de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+pDesvios, 'tab:orange')
plt.axhline(desvioEsperado, color='black', linestyle='dashed', label='Desvío esperado')
plt.xlim(xmin=1)
plt.legend(loc='lower right')

plt.show()

# ------------------------------------------------------------------------------------------

plt.subplot(2, 2, 1)
plt.title("Desvío de las frecuencias relativas de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+dfrecuenciasRelativas, 'tab:pink')
plt.xlim(xmin=1)

plt.subplot(2, 2, 2)
plt.title("Desvío de los promedios de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+dPromedios, 'tab:purple')
plt.xlim(xmin=1)

plt.subplot(2, 2, 3)
plt.title("Desvio de las varianzas de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+dVarianzas, 'tab:blue')
plt.xlim(xmin=1)

plt.subplot(2, 2, 4)
plt.title("Desvío de los desviós de "+str(cantCorridas)+" experimentos")
plt.xlabel("Número de tiradas")
plt.grid(True)
plt.plot([0]+dDesvios, 'tab:orange')
plt.xlim(xmin=1)

plt.show()