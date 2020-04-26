import copy


class Joc:
    lin = 0
    col = 0
    gol = '_'
    jucator = ''
    tabla = None
    JMIN  = None
    JMAX = None

    # initializarea tablei
    def __init__(self, lin, col, tabla = None):
        self.lin = lin
        self.col = col
        if tabla == None:
            self.tabla = [None] * lin
            for i in range(0, lin):
                self.tabla[i] = [self.gol] * col
        else:
            self.tabla = tabla


    def modifica_tabla(self, juc, i, j):
        if i >= self.lin or i < 0 or j >= self.col or j < 0:
            print("Locul ales nu este corect.")
            return False

        if self.tabla[i][j] != "_":
            print("Locul ales este deja ocupat")
            return False
        self.tabla[i][j] = juc
        print("Este randul lui " + juc)
        simb = ""
        if juc == self.JMIN:
            simb = '1'
        else:
            simb = '2'
        if i == 0:
            if j == 0:
                self.tabla[i][j + 1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j+1] = simb
            elif j == self.col - 1:
                self.tabla[i][j-1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j-1] = simb
            else:
                self.tabla[i][j+1] = simb
                self.tabla[i+1][j+1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j-1] = simb
                self.tabla[i][j-1] = simb
        elif i == self.lin - 1:
            if j == 0:
                self.tabla[i][j + 1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j+1] = simb
            elif j == self.col - 1:
                self.tabla[i][j-1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j-1] = simb
            else:
                self.tabla[i][j+1] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j-1] = simb
                self.tabla[i][j-1] = simb
        else:
            if j == 0:
                self.tabla[i][j+1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i+1][j + 1] = simb
            elif j == self.col -1:
                self.tabla[i][j - 1] = simb
                self.tabla[i - 1][j] = simb
                self.tabla[i - 1][j - 1] = simb
                self.tabla[i + 1][j - 1] = simb
                self.tabla[i + 1][j] = simb
            else:
                self.tabla[i][j - 1] = simb
                self.tabla[i][j + 1] = simb
                self.tabla[i - 1][j] = simb
                self.tabla[i + 1][j] = simb
                self.tabla[i-1][j-1] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i + 1][j-1] = simb
                self.tabla[i+1][j+1] = simb
        return True

    def completeaza_in_jurul_jucatorului(self, tabla, juc, i, j, lin, col):

        tabla[i][j] = juc
        simb = ""
        if juc == self.JMIN:
            simb = '1'
        else:
            simb = '2'
        if i == 0:
            if j == 0:
                tabla[i][j + 1] = simb
                tabla[i+1][j] = simb
                tabla[i+1][j+1] = simb
            elif j == col - 1:
                tabla[i][j-1] = simb
                tabla[i+1][j] = simb
                tabla[i+1][j-1] = simb
            else:
                tabla[i][j+1] = simb
                tabla[i+1][j+1] = simb
                tabla[i+1][j] = simb
                tabla[i+1][j-1] = simb
                tabla[i][j-1] = simb
        elif i == lin - 1:
            if j == 0:
                tabla[i][j + 1] = simb
                tabla[i-1][j] = simb
                tabla[i-1][j+1] = simb
            elif j == col - 1:
                tabla[i][j-1] = simb
                tabla[i-1][j] = simb
                tabla[i-1][j-1] = simb
            else:
                tabla[i][j+1] = simb
                tabla[i-1][j+1] = simb
                tabla[i-1][j] = simb
                tabla[i-1][j-1] = simb
                tabla[i][j-1] = simb
        else:
            if j == 0:
                tabla[i][j+1] = simb
                tabla[i-1][j] = simb
                tabla[i+1][j] = simb
                tabla[i-1][j+1] = simb
                tabla[i+1][j + 1] = simb
            elif j == col -1:
                tabla[i][j - 1] = simb
                tabla[i - 1][j] = simb
                tabla[i - 1][j - 1] = simb
                tabla[i + 1][j - 1] = simb
                tabla[i + 1][j] = simb
            else:
                tabla[i][j - 1] = simb
                tabla[i][j + 1] = simb
                tabla[i - 1][j] = simb
                tabla[i + 1][j] = simb
                tabla[i-1][j-1] = simb
                tabla[i-1][j+1] = simb
                tabla[i + 1][j-1] = simb
                tabla[i+1][j+1] = simb
        return tabla

    def verifica_tabla(self):
        for x in range(0, self.lin):
            for y in range(0, self.col):
                if self.tabla[x][y] == '_':
                    return True
        return False

    def scor_jucator(self, jucator):
        if jucator == self.JMIN:
            cauta = '1'
        else:
            cauta = '2'
        nr = 0
        # numar cate simboluri am pentru a vedea care dintre ele are scorul mai bun
        for i in range(self.lin):
            for j in range(self.col):
                if self.tabla[i][j] == cauta:
                    nr = nr + 1
        return nr

    def estimeaza_scor1(self, h):
        # trebuie verificata tabla daca nu a fost umpluta
        if self.verifica_tabla() is False and self.jucator == self.JMAX: # se bazeaza pe maximizarea scorului, fiind JMAX, adica calculatorul
            return 1000 + h
        elif self.verifica_tabla() is False and self.jucator == self.JMIN: # se bazeaza pe minimizarea scorului, fiind JMIN
            return -1000 - h
        # in cazul in care nu ma aflu in niciunul dintre cazurile JMIN sau JMAX, trebuie sa returnez diferenta dintre scorurile celor 2 jucatori
        else:
            return self.scor_jucator(self.JMIN) - self.scor_jucator(self.JMAX)

    def mutari_in_tabla(self, jucator):
        lista_mutari = []
        for i in range(self.lin):
            for j in range(self.col):
                if self.tabla[i][j] == self.gol:
                    tablaNoua = copy.deepcopy(self.tabla)
                    tablaNoua[i][j] = jucator
                    tablaNoua = copy.deepcopy(self.completeaza_in_jurul_jucatorului(tablaNoua, jucator, i, j, self.lin, self.col))
                    lista_mutari.append(Joc(self.lin, self.col, tablaNoua))

        return lista_mutari


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

