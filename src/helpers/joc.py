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
        # initializez tabla ca fiin o matrice de lin linii si col coloane, in functie de datele introduse in linia de comanda
        if tabla == None:
            self.tabla = [None] * lin
            for i in range(0, lin):
                self.tabla[i] = [self.gol] * col
        else:
            self.tabla = tabla

    # trebuie sa modific tabla, primeste ca parametri jucatorul si pozitia untre trebuie sa il pun pe X sau 0
    def modifica_tabla(self, juc, i, j):
        # cat timp nu am iesit din tabla
        if i >= self.lin or i < 0 or j >= self.col or j < 0:
            print("Locul ales nu este corect.")
            return False
        # daca locul ales este deja ocupa, se returneaza False, iar in main se va cere reintroducerea unor coordonate valide
        if self.tabla[i][j] != "_":
            print("Locul ales este deja ocupat")
            return False
        # marchez pe linia i si coloana j jucatorul
        self.tabla[i][j] = juc
        print("Este randul lui " + juc)
        simb = ""
        # daca joc cu JMIN(adica este jucatorul si nu calculatorul), marchez in jurul lui cu 1 - minimizez
        if juc == self.JMIN:
            simb = '1'
        # daca este randul lui JMAX(calculatorul), marchez cu 2 in jurul  lui - maximizez
        else:
            simb = '2'
        # in functie de coordonatele i si j, trebuie sa calculez aria unde voi pune 1 sau 2
        # pot sa marchez in coltul din stanga sus
        if i == 0:
            if j == 0:
                self.tabla[i][j + 1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j+1] = simb
            # coltul din dreapta sus
            elif j == self.col - 1:
                self.tabla[i][j-1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j-1] = simb
            # pe prima linie
            else:
                self.tabla[i][j+1] = simb
                self.tabla[i+1][j+1] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i+1][j-1] = simb
                self.tabla[i][j-1] = simb
        elif i == self.lin - 1:
            # coltul din stanga jos
            if j == 0:
                self.tabla[i][j + 1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j+1] = simb
            # coltul din dreapta jos
            elif j == self.col - 1:
                self.tabla[i][j-1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j-1] = simb
            # pe ultima linie
            else:
                self.tabla[i][j+1] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i-1][j-1] = simb
                self.tabla[i][j-1] = simb
        else:
            # pe prima coloana
            if j == 0:
                self.tabla[i][j+1] = simb
                self.tabla[i-1][j] = simb
                self.tabla[i+1][j] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i+1][j + 1] = simb
            # pe ultima coloana
            elif j == self.col -1:
                self.tabla[i][j - 1] = simb
                self.tabla[i - 1][j] = simb
                self.tabla[i - 1][j - 1] = simb
                self.tabla[i + 1][j - 1] = simb
                self.tabla[i + 1][j] = simb
            # oriunde pe tabla unde este liber
            else:
                self.tabla[i][j - 1] = simb
                self.tabla[i][j + 1] = simb
                self.tabla[i - 1][j] = simb
                self.tabla[i + 1][j] = simb
                self.tabla[i-1][j-1] = simb
                self.tabla[i-1][j+1] = simb
                self.tabla[i + 1][j-1] = simb
                self.tabla[i+1][j+1] = simb
        # returnez true pt ca am putut sa modific tabla
        return True

    # asemenatoare cu functia anterioara, doar ca de data asta primeste si tabla
    # si se va modifica pe tabla primita ca parametru, cu i si j coordonatele pe tabla si nr de linii si coloane
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

    # functia care primeste doar argumentul self verifica daca tabla este plina desimboluri, caz in care trebuie sa se opreasca jocul si sa se stabileasca castigatorul
    # iar in caz contrar, jocul trebuie sa continue
    def verifica_tabla(self):
        for x in range(0, self.lin):
            for y in range(0, self.col):
                if self.tabla[x][y] == '_':
                    return True
        return False

    # functie care primeste jucatorul pt a-i calcula scorul
    def scor_jucator(self, jucator):
        # in functie de jucatorul pe care il am, trebuie sa vad daca maximizez sau minimizez
        # dacasunt pe JMIN, trebuie sa minimizez, ceea ce inseamna ca trebuie sa caut simbolurile de 1
        if jucator == self.JMIN:
            cauta = '1'
        # la JMAX, trebuie sa maximizez, deci caut simbolurile de 2
        else:
            cauta = '2'
        nr = 0
        # numar cate simboluri am pentru a vedea care dintre ele are scorul mai bun
        # in functie de numarul de 1 sau de 2, putem calcula scorul
        for i in range(self.lin):
            for j in range(self.col):
                if self.tabla[i][j] == cauta:
                    nr = nr + 1
        return nr


# fnctie care calculeaza scorul si seteaza h- euristica
    def estimeaza_scor1(self, h):
        # trebuie verificata tabla daca nu a fost umpluta
        if self.verifica_tabla() is False and self.jucator == self.JMAX: # se bazeaza pe maximizarea scorului, fiind JMAX, adica calculatorul
            return 1000 + h
        elif self.verifica_tabla() is False and self.jucator == self.JMIN: # se bazeaza pe minimizarea scorului, fiind JMIN
            return -1000 - h
        # in cazul in care nu ma aflu in niciunul dintre cazurile JMIN sau JMAX, trebuie sa returnez diferenta dintre scorurile celor 2 jucatori
        else:
            return self.scor_jucator(self.JMIN) - self.scor_jucator(self.JMAX)

        # ================================================================================================================================================================================
    # functie asemenatoare cu modifica_tabla de mai sus, primeste jucatorul si unde vreau sa modific, coordonatele i si j
    # modifica taba self
    def modifica_tabla2(self, juc, i, j):
        # daca nu ma aflu in limitele tablei, trebuie reintroduse coordonatele
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
        ii = [-1, -1, -1, 0, 0, 1, 1, 1]
        jj = [-1, 0, 1, -1, 1, -1, 0, 1]
        # de data aceasta, pentru a doua modalitate de calculare a scorului, vreau ca in locurile in care se interesecteaza acoperirea lui X cu cea a lui 0
        # sa nu suprascriu doar cu simbolului celui care a venit "mai tarziu"
        # vreau ca acel loc sa il marchez cu 3 si sa se stie ca este suprapunere
        # in schimb, daca locul este gol, pun simblul corespunzator
        for k in range(8):
            if i + ii[k] >= 0 and i + ii[k] < self.lin and j + jj[k] >= 0 and j + jj[k] < self.col:
                if self.tabla[i + ii[k]][j + jj[k]] != '_':
                    self.tabla[i + ii[k]][j + jj[k]] = '3'
                else:
                    self.tabla[i + ii[k]][j + jj[k]] = simb
        return True
    # functie ce primeste tabla care trebuie modificata, pozitia data de i si j si nr de linii si coloane
    # are rolul de a completa in jurul jucatorului cu simbolul care trebuie, conform explicatiei de la functia anterioara
    def jurul_jucatorului(self, tabla, juc, i, j, lin, col):
        tabla[i][j] = juc
        simb = ""
        if juc == self.JMIN:
            simb = '1'
        else:
            simb = '2'
        ii = [-1, -1, -1, 0, 0, 1, 1, 1]
        jj = [-1, 0, 1, -1, 1, -1, 0, 1]
        for k in range(8):
            if i + ii[k] >= 0 and i + ii[k] < lin and j + jj[k] >= 0 and j + jj[k] < col:
                if tabla[i + ii[k]][j + jj[k]] != '_':
                    tabla[i + ii[k]][j + jj[k]] = '3'
                else:
                    tabla[i + ii[k]][j + jj[k]] = simb
        return tabla

# functie ce primeste jucatorul pt a-i fi calcult scorul
    def scor_jucator2(self, jucator):
        if jucator == self.JMIN:
            cauta = '1'
        else:
            cauta = '2'
        nr = 0
        treiuri = 0
        # numar cate simboluri am pentru a vedea care dintre ele are scorul mai bun
        # de aceasta data, vrem sa vedem doar care dintre jucatori e mai eficient
        # si nu luam in calcul suprapunerile
        for i in range(self.lin):
            for j in range(self.col):
                if self.tabla[i][j] == cauta:
                    nr = nr + 1
                elif self.tabla[i][j] == '3':
                    treiuri = treiuri + 1
        return nr

    def estimeaza_scor2(self, h):
        # trebuie verificata tabla daca nu a fost umpluta
        if self.verifica_tabla() is False and self.jucator == self.JMAX:  # se bazeaza pe maximizarea scorului, fiind JMAX, adica calculatorul
            return 1000 + h
        elif self.verifica_tabla() is False and self.jucator == self.JMIN:  # se bazeaza pe minimizarea scorului, fiind JMIN
            return -1000 - h
        # in cazul in care nu ma aflu in niciunul dintre cazurile JMIN sau JMAX, trebuie sa returnez diferenta dintre scorurile celor 2 jucatori
        else:
            return self.scor_jucator2(self.JMIN) - self.scor_jucator2(self.JMAX)

#=======================================================================================================================================================

# functie ce primeste ca parametru jucatorul
# practic este generarea de mutari succesoare
    def mutari_in_tabla(self, jucator):
        lista_mutari = []
        for i in range(self.lin):
            for j in range(self.col):
                if self.tabla[i][j] == self.gol:
                    tablaNoua = copy.deepcopy(self.tabla)
                    # creez o noua tabla unde pun jucatorul pe pozitia unde este gol
                    # completez tabla conform unei functii de mai sus, depinde de euristica
                    tablaNoua[i][j] = jucator
                    # prima euristica
                    #  tablaNoua = copy.deepcopy(self.completeaza_in_jurul_jucatorului(tablaNoua, jucator, i, j, self.lin, self.col))
                    # a doua euristica
                    tablaNoua = copy.deepcopy(self.jurul_jucatorului(tablaNoua, jucator, i, j, self.lin, self.col))
                    # adaug la lista de mutari posibile noua tabla
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

