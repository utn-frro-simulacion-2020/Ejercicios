from ruleta import Ruleta

# ------------------------------------------------------------------------------------------
# Utils ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# www.geeksforgeeks.org/find-nth-fibonacci-number-using-golden-ratio
def fib ( n ):
    PHI = 1.6180339
    f = [ 0, 1, 1, 2, 3, 5 ]
    if n < 6:
        return f[n]
    t = 5
    fn = 5
    while t < n:
        fn = round(fn * PHI)
        t+=1
    return fn

ruleta = Ruleta()

# ------------------------------------------------------------------------------------------
# Estrategias ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# estrategia Martingale
def estrategiaMartingale(capitalInicial, paridad, AumentoExtra, jugadasMax):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    apuesta = 1
    for  i in range(0,jugadasMax):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial == 0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                apuesta = 1

            elif not res:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                apuesta = apuesta * 2 + AumentoExtra

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))

        else: break

    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}

# ------------------------------------------------------------------------------------------

# estrategia Martingale Inverso
def estrategiaMartingaleInverso(capitalInicial, paridad, jugadasMax):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    apuesta = 1
    for  i in range(0,jugadasMax):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial == 0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                apuesta = apuesta * 2

            elif not res:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                apuesta = 1

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))

        else: break

    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}

# ------------------------------------------------------------------------------------------

# estrategia Fibonacci
# Si se pierde, se sigue adelante con la secuencia
#Cuando ganes, debes volver a dos apuestas hacia atrás en la secuencia descrita y apostar esa cantidad
def estrategiaFibonacci(capitalInicial, paridad, jugadasMax):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    posicionFibonacci = 1
    apuesta = fib(posicionFibonacci)
    for  i in range(0,jugadasMax):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial == 0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                if (posicionFibonacci - 2  <= 0): posicionFibonacci = 1
                else: posicionFibonacci -= 2
                apuesta=fib(posicionFibonacci)

            elif not res:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                posicionFibonacci+=1
                apuesta=fib(posicionFibonacci)

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))

        else: break

    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}

# ------------------------------------------------------------------------------------------

# estrategia Proporción Constante
def estrategiaPropConstante(capitalInicial, proporcion, paridad, jugadasMax):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    prop = proporcion * 0.01
    capitalIteraciones.append(capitalInicial)
    apuesta = capitalIteraciones[-1] * prop
    for  i in range(0,jugadasMax):
        res = ruleta.apostarAParidad(paridad)
        if res:
            apuestasGanadoras += 1
            capitalIteraciones.append(capitalIteraciones[i]+apuesta)

        elif not res:
            capitalIteraciones.append(capitalIteraciones[i]-apuesta)

        frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))
        apuesta = capitalIteraciones[-1] * prop

    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}
