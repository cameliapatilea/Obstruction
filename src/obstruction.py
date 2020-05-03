from helpers.joc import *
from helpers.arg_helper import *
import sys

from helpers.stare import Stare
import time
from helpers.minMax import *
from helpers.alphaBeta import *


def input_mutari():
    print("Introduceti linia si coloana unde doriti sa fie pus simbolul pt a juca")
    print("Daca doriti sa parasiti jocul, introduceti exit")
    if input() == 'exit':
        exit()
    print("Linie = ")
    newLin = int(input())
    print("Coloana = ")
    newCol = int(input())
    return newLin, newCol

def euristica1():
    ture = 0
    tureJucator = 0
    tureCalculator = 0
    linie, coloana, juc, dif, alg, gui = get_arguments(sys.argv[1:])
    linie = int(linie)
    coloana = int(coloana)
    ok = False
    if linie % 2 == 0 or coloana % 2 == 0:
        ok = True

    if ok == False:
        print("Introduceti din nou datele, cel putin linia sau coloana trebuie sa fie un numar par.")
        exit()
    print("Ati ales jucatorul " + juc)
    tabla = Joc(linie, coloana)
    print(str(tabla))

    # avand in vedere ca dimensiunea tablei poate sa fie foarte mare, nu ar fi indicat sa setam adancimea prea mare
    # deoarece exista riscul ca programul sa ocupe tot ram-ul si nu va fi oarte friendly cu calculatorul
    # daca ne dorim o precizie mai mare din partea calculatorului, putem seta adancimea 3 si dimensiunea tablei mai mare

    if dif == "incepator":
        h = 1
    elif dif == "mediu":
        h = 2
    elif dif == "avansat":
        h = 3
    else:
        print("Nivelul introdus nu este unul acceptat")
    Joc.JMIN = juc
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'

    print("Veti juca cu " + juc)
    print("Nivelul de dificultate este " + dif)
    print("\nSa inceapa jocul! Succes!\n")

    # initializarea starii de inceput, cu tabla initializata anterior la prima mutare este goala, jucatorul ales si adancimea data de nivelul de dificutate cerut de jucator
    stare_curenta = Stare(tabla, juc, h)
    # verific daca pe tabla mai pot fi puse simboluri de X sau de 0
    while stare_curenta.tabla_joc.verifica_tabla() is True:
        ture = ture + 1
        print("Este randul lui ", Joc.JMIN)
        # daca ma aflu pe cazul de minimizare
        if stare_curenta.juc_curent == Joc.JMIN:
            t_inainte = int(round(time.time() * 1000))
            tureJucator += 1
            try:
                # se citesc coordonatele(linia si coloana) unde vrea jucatorul sa puna simbolul
                pozX, pozY = input_mutari()
                # daca tabla nu a putu fi modificata(exista deja un simbol sau se afla in proximitatea unui simbol), se vor introduce din nou coordonatele
                while stare_curenta.tabla_joc.modifica_tabla(stare_curenta.juc_curent, pozX, pozY) is False:
                    print("Introduceti din nou coordonatele")
                    pozX, pozY = input_mutari()
                # se schimba jucatorii pentru a putea continua jocul
                stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
            except ValueError:
                print("Linia si coloana trebuie sa fie numare intregi, dintre care cel putin unul par")
            print(str(stare_curenta.tabla_joc))
            print("Scorul jucatorului este ", stare_curenta.scor)
            t_dupa = int(round(time.time() * 1000))
            print("Jucatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
        else:
            print("\nEste randul calculatorului")
            t_inainte = int(round(time.time() * 1000))
            tureCalculator+= 1
            # in functie de algoritmul folosit, se va apela una dintre functii
            if alg == "min-max":
                stare_actualizata = min_max(stare_curenta)
            else:
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)
            # print(stare_actualizata.scor)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta.tabla_joc))
            stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
            print("Scorul calculatorului este ", stare_curenta.scor)
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

    # stiu ca dupa fiecare if schimb jucatorul
    # indiferent care va pune ultimul pe tabla, va intra pe una din conditii si va schimba iarasi jucatorul
    # din aceasta cauza este nevoie ca inainte d eprint sa se mai schimbe inca o data jucatorii intre ei
    stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
    print("\nAu fost nevoie de ", ture, " ture")
    print("\nCastigatorul este " + stare_curenta.juc_curent)
    print("\nJucatorul a jucat ", tureJucator , " ture")
    print("\nCalculatorul a jucat ", tureCalculator, " ture")


def euristica2():
    ture = 0
    tureJucator = 0
    tureCalculator = 0
    linie, coloana, juc, dif, alg, gui = get_arguments(sys.argv[1:])

    linie = int(linie)
    coloana = int(coloana)
    ok = False
    if linie % 2 == 0 or coloana % 2 == 0:
        ok = True

    if ok == False:
        print("Introduceti din nou datele, cel putin linia sau coloana trebuie sa fie un numar par.")
        exit()
    print("Ati ales jucatorul " + juc)
    tabla = Joc(linie, coloana)
    print(str(tabla))

    # avand in vedere ca dimensiunea tablei poate sa fie foarte mare, nu ar fi indicat sa setam adancimea prea mare
    # deoarece exista riscul ca programul sa ocupe tot ram-ul si nu va fi oarte friendly cu calculatorul
    # daca ne dorim o precizie mai mare din partea calculatorului, putem seta adancimea 3 si dimensiunea tablei mai mare
    if dif == "incepator":
        h = 1
    elif dif == "mediu":
        h = 2
    elif dif == "avansat":
        h = 3
    else:
        print("Nivelul introdus nu este unul acceptat")
    Joc.JMIN = juc
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'

    print("Veti juca cu " + juc)
    print("Nivelul de dificultate este " + dif)
    print("Sa inceapa jocul! Succes!")

    # initializarea starii de inceput, cu tabla initializata anterior la prima mutare este goala, jucatorul ales si adancimea data de nivelul de dificutate cerut de jucator
    stare_curenta = Stare(tabla, juc, h)
    # verific daca pe tabla mai pot fi puse simboluri de X sau de 0
    while stare_curenta.tabla_joc.verifica_tabla() is True:

        # daca ma aflu pe cazul de minimizare
        if stare_curenta.juc_curent == Joc.JMIN:
            t_inainte = int(round(time.time() * 1000))
            tureJucator += 1
            if Joc.JMIN == 'X':
                print("\nEste randul lui X")
            else:
                print("\nEste randul lui 0")
            try:

                # se citesc coordonatele(linia si coloana) unde vrea jucatorul sa puna simbolul
                pozX, pozY = input_mutari()
                # daca tabla nu a putu fi modificata(exista deja un simbol sau se afla in proximitatea unui simbol), se vor introduce din nou coordonatele
                while stare_curenta.tabla_joc.modifica_tabla2(stare_curenta.juc_curent, pozX, pozY) is False:
                    print("Introduceti din nou coordonatele")
                    pozX, pozY = input_mutari()
                # se schimba jucatorii pentru a putea continua jocul
                stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
            except ValueError:
                print("Linia si coloana trebuie sa fie numare intregi, dintre care cel putin unul par")
            t_dupa = int(round(time.time() * 1000))
            print("Jucatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
            print(str(stare_curenta.tabla_joc))
            print("Scorul jucatorului este ", stare_curenta.scor)
        else:
            ture = ture + 1
            print("Este randul calculatorului")
            t_inainte = int(round(time.time() * 1000))
            tureCalculator += 1
            # in functie de algoritmul folosit, se va apela una dintre functii
            if alg == "min-max":
                stare_actualizata = min_max(stare_curenta)
            else:
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)
            # print(stare_actualizata.scor)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta.tabla_joc))
            print("\nScorul calculatorului este ", stare_curenta.scor)
            stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

    # stiu ca dupa fiecare if schimb jucatorul
    # indiferent care va pune ultimul pe tabla, va intra pe una din conditii si va schimba iarasi jucatorul
    # din aceasta cauza este nevoie ca inainte d eprint sa se mai schimbe inca o data jucatorii intre ei
    stare_curenta.juc_curent = Stare.schimba_jucator(stare_curenta.juc_curent)
    print("\nCastigatorul este " + stare_curenta.juc_curent)
    print("\nAu fost nevoie de " , ture, " ture")
    print("\nJucatorul a jucat ", tureJucator, " ture")
    print("\nCalculatorul a jucat ", tureCalculator, " ture")

if __name__ == '__main__':
    t1 = int(round(time.time() * 1000))
    # euristica1()
    euristica2()
    t2 = int(round(time.time() * 1000))
    print("\nProgramul a rulat timp de ", t2-t1, " milisecunde")


