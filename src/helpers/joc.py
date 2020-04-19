class Joc:
    lin = 0
    col = 0
    gol = '_'

    # initializarea tablei
    def __init__(self, lin, col):
        self.lin = lin
        self.col = col
        self.tabla = [None] * lin
        for i in range(0, lin):
            self.tabla[i] = [self.gol] * col

    def __str__(self):
        matrice = ""
        for i in range(0, self.lin):
            linie = " ".join(self.tabla[i]) + "\n"
            matrice = matrice + linie
        return matrice

    def __repr__(self):
        matrice = ""
        for i in range(0, self.lin):
            linie = " ".join(self.tabla[i]) + "\n"
            matrice = matrice + linie
        return matrice

    