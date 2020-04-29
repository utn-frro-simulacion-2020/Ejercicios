import random as random

class Ruleta:
    def generarTirada(self):
        return random.randint(0,36)
    
    def apostarAParidad(self, paridadApostada):
        nro = self.generarTirada()
        if nro == 0:
            return False
        if paridadApostada == "p" and nro % 2 == 0:
            return True
        elif paridadApostada == "i" and nro % 2 == 1:
            return True
        return False