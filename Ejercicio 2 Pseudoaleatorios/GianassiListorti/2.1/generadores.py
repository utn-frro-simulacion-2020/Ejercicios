import numpy as np
import random as rand

class GeneradorMiddleSquare:
    seed = 0
    def __init__(self, seed):
        self.seed = seed

    def gen(self):
        if len(str(self.seed)) == 4:
            square = num * num
            if len(str(square)) < 8:
                need = 8 - len(str(square))
                addZero = ""
                for i in range(0,need):
                    addZero = str(0) + addZero
                square = addZero + str(square)  
            else: 
                square = str(square)
                result = int(square[2] + square[3] + square[4] + square[5])
            yield result
    
    def muestra(self, n, interval):
        lower, upper = interval[0], interval[1]
        sample = []
        glibc = self.gen()
        for i in range(n):
            observation = (upper - lower) * (next(glibc) / (m - 1)) + lower
            sample.append(int(observation))
        return sample

                
                

class GeneradorGCL:
    seed = 0

    def __init__(self, seed):
        self.seed = seed

    def gen(self, a,c,m):     
        xi = self.seed
        while True:
            xf = (a * xi + c) % m
            xi = xf
            yield xf

    def muestra(self, n, interval):
        lower, upper = interval[0], interval[1]
        sample = []
        # parameters as in GNU C Library
        a = 1103515245 #Multiplicador
        c = 12345 #Incremento
        m = 2**32 #Modulo
        glibc = self.gen(a,c,m)
        for i in range(n):
            observation = (upper - lower) * (next(glibc) / (m - 1)) + lower
            sample.append(int(observation))

        return sample