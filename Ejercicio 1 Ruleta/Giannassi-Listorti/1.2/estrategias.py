from ruleta import Ruleta

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

def Martingala(capitalInicial, paridad, apuestaInicial, iteraciones):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    posicionFibonacci = 1
    apuesta = fib(posicionFibonacci)
    for  i in range(0,iteraciones):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial == 0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                apuesta = apuestaInicial

            else:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                apuesta = apuesta * 2

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))

        else: break

    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}

def Dalembert(capitalInicial, paridad, apuestaInicial, iteraciones): #tiene apuesta inicial 1
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones = []
    capitalIteraciones.append(capitalInicial)
    apuesta = apuestaInicial
    for i in range(0,iteraciones):
        if(capitalIteraciones[i]>=apuesta and capitalInicial!=0) or capitalInicial==0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                apuesta = apuesta-1

            else:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                apuesta = apuesta + 1

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))
        else: break
    
    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}

def Fibonacci(capitalInicial, paridad, apuestaInicial, iteraciones):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones = []
    capitalIteraciones.append(capitalInicial)
    posicionFibonacci = 1
    apuesta = fib(posicionFibonacci)
    for  i in range(0,iteraciones):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial == 0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                if (posicionFibonacci - 2  <= 0): posicionFibonacci = 1
                else: posicionFibonacci -= 2
                apuesta=fib(posicionFibonacci)

            else:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                posicionFibonacci+=1
                apuesta=fib(posicionFibonacci)

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))

        else: break
    
    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}