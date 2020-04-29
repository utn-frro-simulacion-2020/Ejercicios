import matplotlib.pyplot as plt

def graficarResultado(capitalInicial, resultado):
    plt.title("xxxxx")
    plt.xlabel("xxxx")
    plt.grid(True)
    plt.plot([0]+resultado, 'tab:pink', label='xxxxxxxxx')
    plt.axhline(capitalInicial, color='black', linestyle='dashed', label='Frecuencia relativa esperada')
    plt.xlim(xmin=1)
    plt.legend(loc='upper right')
    plt.show()