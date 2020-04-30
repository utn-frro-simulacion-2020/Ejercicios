import matplotlib.pyplot as plt

def graficarResultados(resultados):

    plt.subplot(1, 2, 1)
    plt.title("Dinero en caja")
    plt.xlabel("n° de tirada")
    plt.grid(True)
    for r in resultados:
        plt.plot(r['capital'])
    if resultados[0]['capital'][0] != 0:
        plt.axhline(resultados[0]['capital'][0], color='black', linestyle='dashed', label='Capital inicial')
        plt.legend(loc='lower right')

    plt.subplot(1, 2, 2)
    plt.title("Frecuencia relativa de apuestas ganadas")
    plt.xlabel("n° de tirada")
    plt.grid(True)
    for r in resultados:
        plt.plot([0]+r['frecuencia'])
    plt.axhline(0.486486486, color='black', linestyle='dashed', label='Frecuencia esperada')
    plt.xlim(xmin=1)
    plt.legend(loc='lower right')

    plt.show()
