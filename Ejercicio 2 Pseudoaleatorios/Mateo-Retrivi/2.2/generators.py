import random
import math


def rand():
    return random.uniform(0, 1)

# --------------------------------------


def randomUniform(a, b):
    return rand() * (b - a) + a


def randomExponential(lamb):
    return -(1 / lamb) * (math.log(rand()))


def randomGamma(alpha, k):
    tr = 1.0
    for _ in range(0, k):
        tr *= rand()
    return -(1 / alpha) * math.log(tr)


def randomNormal(mu, sigma, k):
    sum = 0
    for _ in range(0, k):
        sum += rand()
    return sigma * math.sqrt((12 / k)) * (sum - (k / 2)) + mu


def randomPascal(k, q):
    multiplier = 1
    for _ in range(0, k):
        multiplier *= rand()
    x = math.log(multiplier) / math.log(q)
    return math.floor(x)


def randomBinomial(n, p):
    x = 0
    for _ in range(0, n):
        if (rand() - p) <= 0:
            x += 1
    return x


def randomHypergeometric(N, n, p):
    x = 0.0
    for _ in range(1, n):
        r = rand()
        if (r - p) <= 0:
            s = 1
            x += 1
        else:
            s = 0
        p = (N * p - s) / (N - 1)
        N -= 1
    return x


def randomPoisson(lamb):
    x = 0
    multiplier = 1.0
    b = math.exp(-lamb)
    while True:
        multiplier *= rand()
        if multiplier > b:
            x += 1
        else:
            break
    return x


def randomEmpirical():
    p = [0.143, 0.037, 0.186, 0.018, 0.234, 0.078, 0.144, 0.061, 0.047, 0.052]
    r = rand()
    acum = 0
    x = 1
    for i in p:
        acum += i
        if (r < acum):
            break
        else:
            x += 1
    return x
