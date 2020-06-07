from tkinter import *
import math
import matplotlib.pyplot as plt


def graphicDisplay(numbers):
    size = math.floor(math.sqrt(len(numbers)))
    master = Tk()
    padding = 10
    w = Canvas(master, width=size + padding * 2, height=size + padding * 2)
    w.pack()

    greater = 0
    for i in range(0, size):
        for j in range(0, size):
            if round(numbers[size * i + j]) == 1:
                greater += 1
                w.create_line(j + padding, i + padding, j +
                              padding + 1, i + padding, fill="#000000")

    greaterProp = greater / (size * size)
    w.create_rectangle(padding, size + padding - 50, size * greaterProp,
                       size + padding - 30, outline="#22a602", fill="#22a602")
    w.create_rectangle(padding, size + padding - 25, size * (1 - greaterProp),
                       size + padding - 5, outline="#ff8200", fill="#ff8200")
    w.create_text(padding + 10, size + padding - 40, fill="black",
                  text="Mayor a 0.5: " + "{:.4f}".format(greaterProp), anchor=W)
    w.create_text(padding + 10, size + padding - 15, fill="black",
                  text="Menor a 0.5: " + "{:.4f}".format(1 - greaterProp), anchor=W)

    master.mainloop()


def chiSquareTest(numbers):
    # Calculo de frecuencia relativa
    sortedNumbers = sorted(numbers)
    n = len(numbers)
    absFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    interval = 0
    for i in range(0, 10):
        for j in range(0, n):
            if interval <= sortedNumbers[j] < (interval + 0.1):
                absFreq[i] += 1
        interval += 0.1

    # Calculo sumatoria de frecuencia relativa al cuadrado
    chiSquare = 0
    for k in range(0, 10):
        chiSquare += (((absFreq[k]) - (n/10)) ** 2)/(n/10)

    # Compara X^2 con el valor de la tabla en df=9
    if (chiSquare) < 16.92:
        return "Aprobado"
    else:
        return "Rechazado"


def parityTest(numbers):
    odd = 0
    even = 0
    n = len(numbers)

    for i in range(0, n):
        if (math.floor(numbers[i] * 10000) % 2) == 0:
            even += 1
        else:
            odd += 1

    answer = (((even - (n/2))**2) + ((odd - (n/2))**2)) * (2/n)

    # df=1

    if (answer < 3.84):
        return "Aprobado"
    else:
        return "Rechazado"


def kolmogorovSmirnovTest(numbers):
    n = len(numbers)
    D_plus = []
    D_minus = []

    # Rank the N random numbers
    sortedList = numbers.copy()
    sortedList.sort()

    # Calculate max(i/N-Ri)
    for i in range(1, n + 1):
        x = i / n - sortedList[i-1]
        D_plus.append(x)

    # Calculate max(Ri-((i-1)/N))
    for i in range(1, n + 1):
        y = (i-1)/n
        y = sortedList[i-1]-y
        D_minus.append(y)

    # Calculate max(D+, D-)
    ans = max(max(D_plus, D_minus))
    expected = 1.36/math.sqrt(n)
    if (ans < expected):
        return "Aprobado"
    else:
        return "Rechazado"


def pokerTest(numbers):

    allEquals = 0
    twoEquals = 0
    allDiferents = 0

    expectedAllEquals = 0.01 * len(numbers)
    expectedTwoEquals = 0.27 * len(numbers)
    expectedAllDiferents = 0.72 * len(numbers)

    for i in range(0, len(numbers)):

        fp = str(numbers[i]-int(numbers[i]))[1:]
        while True:
            if len(fp) < 4:
                fp = fp + "0"
            else:
                break
        fp = (fp[slice(1, 4)])

        if fp[0] == fp[1] == fp[2]:
            allEquals += 1
        elif fp[0] != fp[1] and fp[1] != fp[2] and fp[0] != fp[2]:
            allDiferents += 1
        else:
            twoEquals += 1

    x1 = (pow((allDiferents - expectedAllDiferents), 2))/expectedAllDiferents
    x2 = (pow((twoEquals - expectedTwoEquals), 2))/expectedTwoEquals
    x3 = (pow((allEquals - expectedAllEquals), 2))/expectedAllEquals

    if (x1 + x2 + x3 < 5.99):
        return "Aprobado"
    else:
        return "Rechazado"


def runAllTests(numbers, name):

    colLabels = ("Generador", "Poker Test", "Chi Square Test",
                 "Kolmogorov-Smirnov Test", "Parity Test")
    cellText = [[name, str(pokerTest(numbers)), str(chiSquareTest(numbers)), str(
        kolmogorovSmirnovTest(numbers)), str(parityTest(numbers))]]

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    table = ax.table(cellText=cellText, colLabels=colLabels,
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    fig.tight_layout()
    plt.show()

    graphicDisplay(numbers)
