from helpers.joc import *


def alpha_beta(alpha, beta, stare):
    # daca am ajuns pe o frunza sau pe tabla nu mai pot fi puse simboluri, inseamna ca tabla este completa si trebuie sa oprim jocul
    if stare.adancime == 0 or stare.tabla_joc.verifica_tabla() is False:
        stare.scor = stare.tabla_joc.estimeaza_scor1(stare.adancime)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    # obtinu lista de mutari posibile generata in clasa Stare
    stare.mutari_posibile = stare.mutari_stare()

    # daca ma aflu pe jucatorul introdus din consola, inseamna ca trebuie sa minimizez - JMIN
    if stare.juc_curent == Joc.jucator:
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    # daca nu sunt pe jucatorul "calculator", adica pe JMAX trebuie sa maximizez
    elif stare.juc_curent != Joc.jucator:
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break

    stare.scor = stare.stare_aleasa.scor

    return stare