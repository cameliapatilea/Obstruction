from helpers.joc import Joc


def min_max(stare):
    # daca am ajuns pe o frunza sau pe tabla nu mai pot fi puse simboluri, inseamna ca tabla este completa si trebuie sa oprim jocul
    if stare.adancime == 0 or stare.tabla_joc.verifica_tabla() is False:
        # a doua euristica
        stare.scor = stare.tabla_joc.estimeaza_scor2(stare.adancime)
        # prima euristica
        # stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(x) for x in stare.mutari_posibile]

    if stare.juc_curent == Joc.jucator:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor = stare.stare_aleasa.scor
    return stare