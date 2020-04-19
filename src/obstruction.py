from helpers.joc import *
from helpers.arg_helper import *
import sys


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
    print(str(tabla))

    while tabla.verifica_tabla() is True:
        pozX, pozY = input_mutari()

        while tabla.modifica_tabla(juc, pozX, pozY) is False:
            print("Introduceti din nou coordonatele")
            pozX, pozY = input_mutari()
        print(str(tabla))


