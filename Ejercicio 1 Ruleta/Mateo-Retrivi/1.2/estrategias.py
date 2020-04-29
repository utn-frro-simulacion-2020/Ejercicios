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

# Estrategias ------------------------------------------------------------------------------


# estrategia Martingale
def estrategiaMartingale(capitalInicial):
    return [1,2,3,4,5]


# estrategia Fibonacci
# Si se pierde, se sigue adelante con la secuencia
#Cuando ganes, debes volver a dos apuestas hacia atrás en la secuencia descrita y apostar esa cantidad
def estrategiaFibonacci(capitalInicial,paridad):
    capitalIteraciones=[]
    capitalIteraciones.append(capitalInicial)
    posicionFibonacci = 1
    apuesta = fib(posicionFibonacci)
    for  i in range(0,50000):
        if (capitalIteraciones[i] >= apuesta and capitalInicial!=0) or capitalInicial==0:
            res = ruleta.apostarAParidad(paridad)
            if res:
                capitalIteraciones.append(capitalIteraciones[i]+apuesta)
                if (posicionFibonacci - 2  <= 0): posicionFibonacci = 1
                else: posicionFibonacci -= 2
                apuesta=fib(posicionFibonacci)
               
            elif not res:
                capitalIteraciones.append(capitalIteraciones[i]-apuesta)
                posicionFibonacci+=1
                apuesta=fib(posicionFibonacci)
               
        else: break

    return capitalIteraciones