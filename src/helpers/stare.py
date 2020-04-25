
class Stare:
    def __init__(self, tabla_joc, juc_curent, adancime, parinte = None, scor = None):
        self.tabla_joc = tabla_joc
        self.juc_curent = juc_curent
        self.adancime = adancime
        self.scor = scor
        self.mutari_posibile = []
        self.stare_aleasa  =None

    # schimbarea jucatorului se face in main(fisierul obstruction.py)
    def schimba_jucator( jucator):
        if jucator == 'X':
            return '0'
        else:
            return 'X'

    def mutari_stare(self):
        lista_mutari = self.tabla_joc.mutari_in_tabla(self.juc_curent)
        juc_opus = Stare.schimba_jucator(self.juc_curent)
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte = self) for mutare in lista_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucatorul care a marcat acum a fost:" + self.juc_curent + ")\n"
        return sir
