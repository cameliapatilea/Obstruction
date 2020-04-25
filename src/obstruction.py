from helpers.joc import *
from helpers.arg_helper import *
import sys

from helpers.stare import Stare
import time
from helpers.minMax import *
from helpers.alphaBeta import *


def input_mutari():
    print("Introduceti linia si coloana unde doriti sa fie pus simbolul pt a juca")
    print("Linie = ")
    newLin = int(input())
    print("Coloana = ")
    newCol = int(input())
    return newLin, newCol




if __name__ == '__main__':

    linie, coloana, juc, dif, alg, gui = get_arguments(sys.argv[1:])
    linie = int(linie)
    coloana = int(coloana)
    ok = False
    print("Ati ales jucatorul " + juc)
    tabla = Joc(linie, coloana)
    # print(str(tabla))


    Joc.JMIN = juc
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'


    # lista = tabla.mutari_in_tabla(juc)
    """for i in lista:
        print(str(i))"""

    """ while tabla.verifica_tabla() is True:

        pozX, pozY = input_mutari()

        while tabla.modifica_tabla(juc, pozX, pozY) is False:
            print("Introduceti din nou coordonatele")
            pozX, pozY = input_mutari()
        juc = Stare.schimba_jucator(juc)

        print(str(tabla))"""

    """juc = Stare.schimba_jucator(juc)
    print("Castigatorul este " + juc)"""

# adancime 1 -incepator
# adancime 2- mediu
# adancime 3- avansat
    stare_curenta = Stare(tabla, juc, 3)
    while stare_curenta.tabla_joc.verifica_tabla() is True:
        if stare_curenta.juc_curent == Joc.JMIN:
            raspuns_valid = False
            try:
                pozX, pozY = input_mutari()
                while stare_curenta.tabla_joc.modifica_tabla(stare_curenta.juc_curent, pozX, pozY) is False:
                    print("Introduceti din nou coordonatele")
                    pozX, pozY = input_mutari()
                stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
            except ValueError:
                print("Linia si coloana trebuie sa fie numare intregi, dintre care cel putin unul par")
            # print(str(stare_curenta.tabla_joc))
        else:
            t_inainte = int(round(time.time() * 1000))
            if alg == "min-max":
                stare_actualizata = min_max(stare_curenta)
            else:
                stare_actualizata = alpha_beta(-5000,5000,stare_curenta)
            print(stare_actualizata.scor)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta.tabla_joc))
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
            stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
        # print(str(stare_curenta.tabla_joc))
    stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
    print("Castigatorul este " + stare_curenta.juc_curent)

