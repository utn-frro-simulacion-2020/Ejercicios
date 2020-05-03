from ruleta import Ruleta

def fib_gen(prev, num):
    prev, num = prev, n
    while(True):
        yield prev, num
        prev, num = num, prev+num

ruleta = Ruleta()

def Martingala(capitalInicial, paridad, apuestaInicial, iteraciones):
    apuestasGanadoras = 0
    frecuenciaDeGanadas = []
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    apuesta = apuestaInicial
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
    generadorFib = fib_gen(apuestaInicial)
    prev,apuesta = next(generadorFib)
    for i in range(0, iteraciones):
        if(capitalIteraciones[i]>=apuesta and capitalInicial!=0) or capitalInicial==0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                apuestasGanadoras += 1
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                if(prev!=0):
                    apuesta=prev
                else:
                    apuesta=apuestaInicial

            else:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                prev, apuesta = next(generadorFib)

            frecuenciaDeGanadas.append(apuestasGanadoras/(i+1))
        else: break
    
    return {'capital' : capitalIteraciones, 'frecuencia': frecuenciaDeGanadas}