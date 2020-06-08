import matplotlib.pyplot as plt


class Graficadores:
    def graficarUniforme(self, u):
        plt.title("uniforme")
        plt.hist(u)
        plt.show()

    def graficarGamma(self, g):
        plt.title("gamma")
        plt.hist(g, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()

    def graficarPascal(self, p):
        plt.title("pascal")
        plt.hist(p, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()

    def graficarExponencial(self, e):
        plt.title("exponencial")
        plt.hist(e, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='g')
        plt.show()

    def graficarNormal(self, n):
        plt.title("normal")
        plt.hist(n, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='y')
        plt.show()

    def graficarBinomial(self, b):
        plt.title("binomial")
        plt.hist(b, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()

    def graficarPoisson(self, po):
        plt.title("poisson")
        plt.hist(po, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()

    def graficarEmpirica(self, em):
        plt.title("empírica discreta")
        plt.hist(em, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()
    
    def graficarHipergeo(self, hip):
        plt.title("hipergeométrica")
        plt.hist(hip, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()