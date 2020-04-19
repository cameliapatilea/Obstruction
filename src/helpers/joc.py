class Joc:
    lin = 0
    col = 0
    gol = '_'
    jucator = ''

    # initializarea tablei
    def __init__(self, lin, col):
        self.lin = lin
        self.col = col
        self.tabla = [None] * lin
        for i in range(0, lin):
            self.tabla[i] = [self.gol] * col

    def modifica_tabla(self, juc, i, j):
        if i > self.lin or i < 0 or j > self.col or j < 0:
            print("Locul ales nu este corect.")
            return False

        if self.tabla[i][j] != "_":
            print("Locul ales este deja ocupat")
            return False
        self.tabla[i][j] = juc
        if i == 0:
            if j == 0:
                self.tabla[i][j + 1] = "#"
                self.tabla[i+1][j] = "#"
                self.tabla[i+1][j+1] = "#"
            elif j == self.col - 1:
                self.tabla[i][j-1] = "#"
                self.tabla[i+1][j] = "#"
                self.tabla[i+1][j-1] = "#"
            else:
                self.tabla[i][j+1] = "#"
                self.tabla[i+1][j+1] = "#"
                self.tabla[i+1][j] = "#"
                self.tabla[i+1][j-1] = "#"
                self.tabla[i][j-1] = "#"
        elif i == self.lin - 1:
            if j == 0:
                self.tabla[i][j + 1] = "#"
                self.tabla[i-1][j] = "#"
                self.tabla[i-1][j+1] = "#"
            elif j == self.col - 1:
                self.tabla[i][j-1] = "#"
                self.tabla[i-1][j] = "#"
                self.tabla[i-1][j-1] = "#"
            else:
                self.tabla[i][j+1] = "#"
                self.tabla[i-1][j+1] = "#"
                self.tabla[i-1][j] = "#"
                self.tabla[i-1][j-1] = "#"
                self.tabla[i][j-1] = "#"
        else:
            if j == 0:
                self.tabla[i][j+1] = "#"
                self.tabla[i-1][j] = "#"
                self.tabla[i+1][j] = "#"
                self.tabla[i-1][j+1] = "#"
                self.tabla[i+1][j + 1] = "#"
            elif j == self.col -1:
                self.tabla[i][j - 1] = "#"
                self.tabla[i - 1][j] = "#"
                self.tabla[i - 1][j - 1] = "#"
                self.tabla[i + 1][j - 1] = "#"
                self.tabla[i + 1][j] = "#"
            else:
                self.tabla[i][j - 1] = "#"
                self.tabla[i][j + 1] = "#"
                self.tabla[i - 1][j] = "#"
                self.tabla[i + 1][j] = "#"
                self.tabla[i-1][j-1] = "#"
                self.tabla[i-1][j+1] = "#"
                self.tabla[i + 1][j-1] = "#"
                self.tabla[i+1][j+1] = "#"
        return True

    def verifica_tabla(self):
        for x in range(0, self.lin):
            for y in range(0, self.col):
                if self.tabla[x][y] == '_':
                    return True
        return False

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

