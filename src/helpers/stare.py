
class Stare:
    def __init__(self, tabla_joc, juc_curent, adancime, parinte = None, scor = None):
        self.tabla_joc = tabla_joc
        self.juc_curent = juc_curent
        self.adancime = adancime
        self.scor = scor
        self.mutari_posibile = []
        self.stare_aleasa  =None


    # primeste ca parametru jucatorul si in functie de care este, il returneaza pe celalalt
    def schimba_jucator( jucator):
        if jucator == 'X':
            return '0'
        else:
            return 'X'

# primeste ca parametru doarself
    def mutari_stare(self):
        # iau lista de mutari pentru jucatorul curent
        lista_mutari = self.tabla_joc.mutari_in_tabla(self.juc_curent)
        # trebuie sa schimb jucatorul si apelez functia de mai sus
        juc_opus = Stare.schimba_jucator(self.juc_curent)
        # pentru fiecare mutare in lista de mutari, trebuie sa generez o lista de stari
        # si trebuie sa scad de fiecare data in adancime pana ajung la adancimea 0
        # de fiecare data voi creea o noua stare cu jucatorul opus, mutarea respectiva din lista de mutari, un pas mai putin la adancime
        # iar parintele va deveni starea curenta
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte = self) for mutare in lista_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucatorul care a marcat acum a fost:" + self.juc_curent + ")\n"
        return sir
