import math
import scipy.stats
from scipy.stats import norm


def squareChiUniform(sample):
    print('Test Chi Cuadrado para distribución uniforme:')
    valorTabla = 16.9190  # con alpha 0.05 y grado de libertad 9
    freq_esperada = len(sample)/10
    frecuencias = [] * 10
    intervalos = [0] * 10
    # divido la muestra en 10 intervalos
    for i in range(0, len(sample)):
        if(sample[i] < 0.1):
            intervalos[0] = intervalos[0] + 1
        elif(sample[i] < 0.2):
            intervalos[1] = intervalos[1] + 1
        elif(sample[i] < 0.3):
            intervalos[2] = intervalos[2] + 1
        elif(sample[i] < 0.4):
            intervalos[3] = intervalos[3] + 1
        elif(sample[i] < 0.5):
            intervalos[4] = intervalos[4] + 1
        elif(sample[i] < 0.6):
            intervalos[5] = intervalos[5] + 1
        elif(sample[i] < 0.7):
            intervalos[6] = intervalos[6] + 1
        elif(sample[i] < 0.8):
            intervalos[7] = intervalos[7] + 1
        elif(sample[i] < 0.9):
            intervalos[8] = intervalos[8] + 1
        else:
            intervalos[9] = intervalos[9] + 1

    for i in range(0, len(frecuencias)):
        frecuencias[i] = (intervalos[i] - freq_esperada)**2/freq_esperada

    suma = sum(frecuencias)

    if(suma < valorTabla):
        print("Test aprobado. muestra uniforme")
        return True
    else:
        print("Test desaprobado. No implica que no sea uniforme")
        return False


def squareChiExponential(sample):
    print("Test Chi Cuadrado para distribucion exponencial:")
    observado = []
    esperado = []
    c = 0.3
    chiquadesperado = round(scipy.stats.chi2.ppf(1-0.05, 9), 2)
    for i in range(9):
        x = 0
        for j in range(len(sample)):
            if (c-0.3) <= float(sample[j]) <= c:
                x += 1
        observado.append(x)
        esperado.append(1000*((1-(math.e)**(-(1/5)*c)) -
                              (1-(math.e)**(-(1/5)*(c-0.3)))))
        c += 0.3
    observado.append(1000-sum(observado))
    esperado.append(1000*((math.e)**(-(1/5)*(c-0.3))))
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i]-esperado[i])**2)/esperado[i])
        x2 += x1
    if (x2 < chiquadesperado):
        print("Test aprobado. muestra exponencial")
        return True
    else:
        print("Test desaprobado. No implica que no sea exponencial")
        return False


def squareChiNormal(sample):
    print("Test Chi Cuadrado para distribucion Normal")
    observado = []
    esperado = []
    a1 = 0
    a2 = 0
    chiquadesperado = round(scipy.stats.chi2.ppf(1-0.05, 9), 2)
    c = -80
    for i in range(10):
        x = 0
        for j in range(len(sample)):
            if (c-20) <= float(sample[j]) <= c:
                x += 1
        observado.append(x)
        a1 += (c-10)*x
        a2 += ((c-10)**2)*x
        c += 20
    a1 = a1/1000
    a2 = a2/1000
    desviacion = math.sqrt(a2-a1**2)
    media = a1
    c = -80
    esperado = []
    for i in range(10):
        esperado.append(1000*(norm.cdf((c-media)/desviacion) -
                              norm.cdf(((c-20)-media)/desviacion)))
        c += 20
    x2 = 0
    for i in range(len(observado)):
        x1 = (((observado[i]-esperado[i])**2)/esperado[i])
        x2 += x1
    if (x2 < chiquadesperado):
        print("Test aprobado. muestra normal")
        return True
    else:
        print("No paso el test")
        return False
