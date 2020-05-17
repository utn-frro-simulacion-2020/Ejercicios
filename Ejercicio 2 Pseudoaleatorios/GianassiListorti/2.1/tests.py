from math import sqrt
import numpy as np
import collections

def testParidad(muestra):
    n = len(muestra)
    mult = 100000000
    muestraArreglada = []
    for i in range(0,n):
        num = str(int(np.trunc(muestra[i]*mult)))
        if num==str(0):
            muestraArreglada.append(0)
        else:
            muestraArreglada.append(int(num[0] + num[1] + num[2] + num[3]))
    x = 0
    for m in muestraArreglada:
        if m % 2 == 0:
            x = x + 1
    frecuencia = x/n
    if frecuencia >=0.45 and frecuencia <= 0.55:
        return True
        print("Test aprobado. Muestra aleatoria, las frecuencias de las paridades se encuentran en el rango de aceptación")
    else: 
        print("Test desaprobado. Muestra con números mayormente de una paridad notablemente")
        return False

    return None
                
    



def kstest(muestra):
    muestra = sorted(muestra)
    d_plus = []
    d_minus = []
    esperada = 1.36/sqrt(len(muestra)) # Generalización de fórmula de una tabla

    for i in range(1, len(muestra)+1):
        x= i/len(muestra) - muestra[i-1]
        d_plus.append(x)

    for i in range(1, len(muestra) + 1): 
        y =(i-1)/len(muestra)
        y =muestra[i-1]-y 
        d_minus.append(y)

    # Calculate max(D+, D-) 
    ans = max(max(d_plus, d_minus)) 
    if(ans<esperada):
        print("Test aprobado. Muestra uniforme")
        return True
    else:
        print("Test desaprobado. No implica que no sea uniforme")
        return False
    

def rachasArribaAbajoMediaTest(muestra):
    listaOperadores = []
    N = len(muestra)
    n1 = 0
    n2 = 0
    b = 0
    mediaMuestra = np.average(muestra)
    mediaB = 0
    varianzaB = 0
    Z = 0
    for l in muestra:
        if l >= mediaMuestra:
            listaOperadores.append('+')
            n1 = n1 + 1 
        else:
            listaOperadores.append('-')
            n2 = n2 + 1
    for j in range(0,len(listaOperadores)-1):
        if listaOperadores[j] == '+':
            if listaOperadores[j] != listaOperadores[j+1]:
                b = b + 1
        else:
            if listaOperadores[j] != listaOperadores[j+1]:
                b = b + 1
    mediaB = ((2*n1*n2)/(n1+n2))+1
    varianzaB = (2*n1*n2*((2*n1*n2)-N))/(N*N*(N-1))
    Z = (b - mediaB)/(np.sqrt(varianzaB))
    #alfa = 0.05 , por lo tanto Z(1-(alfa/2)) = 1.96
    if abs(Z)<1.96:
        print("Test aprobado. Se demuestra la Independecia, por lo tanto, la aleatoriedad también")
        return True
    else:
        print("Test desaprobado. Se rechaza la independencia")
        return False
            
def chiCuadrado(muestra):
    valorTabla = 16.9190 # con alpha 0.05 y grado de libertad 9
    freq_esperada = len(muestra)/10
    frecuencias = [] * 10
    intervalos = [0] * 10
    #divido la muestra en 10 intervalos
    for i in range(0, len(muestra)):
        if(muestra[i]<0.1): intervalos[0] = intervalos[0] + 1
        elif(muestra[i]<0.2): intervalos[1] = intervalos[1] + 1
        elif(muestra[i]<0.3): intervalos[2] = intervalos[2] + 1
        elif(muestra[i]<0.4): intervalos[3] = intervalos[3] + 1
        elif(muestra[i]<0.5): intervalos[4] = intervalos[4] + 1
        elif(muestra[i]<0.6): intervalos[5] = intervalos[5] + 1
        elif(muestra[i]<0.7): intervalos[6] = intervalos[6] + 1
        elif(muestra[i]<0.8): intervalos[7] = intervalos[7] + 1
        elif(muestra[i]<0.9): intervalos[8] = intervalos[8] + 1
        else: intervalos[9] = intervalos[9] + 1

    for i in range(0, len(frecuencias)):
        frecuencias[i] = (intervalos[i]- freq_esperada)**2/freq_esperada

    suma = sum(frecuencias)

    if(suma<valorTabla):
        print("Test aprobado. Muestra uniforme")
        return True
    else:
        print("Test desaprobado. No implica que no sea uniforme")
        return False