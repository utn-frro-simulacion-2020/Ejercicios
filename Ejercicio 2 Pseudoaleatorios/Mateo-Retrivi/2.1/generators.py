import random


def linealCongruentialGenerator(seed, modulus, increment, multiplier, nReturn):
    randomList = []
    for _ in range(0, nReturn):
        seed = (seed * multiplier + increment) % modulus
        randomList.append(seed / modulus)
    return randomList


def middleSquareGenerator(seed, nReturn):
    length = len(str(seed))
    randomList = []
    for _ in range(0, nReturn):
        square = str(seed * seed)
        while True:
            if len(square) < length * 2:
                square = "0" + square
            else:
                break
        seed = int(square[slice(int(-3 * length / 2), int(-length / 2))])
        randomList.append(float("0." + str(seed)))
    return randomList


def pythonRandom(nReturn):
    randomList = []
    for _ in range(0, nReturn):
        randomList.append(random.uniform(0, 1))
    return randomList
