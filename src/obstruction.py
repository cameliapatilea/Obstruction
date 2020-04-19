from src.helpers.joc import *
from src.helpers.arg_helper import *
import sys


if __name__ == '__main__':
    linie, coloana, juc, dif, alg, gui = get_arguments(sys.argv[1:])
    linie = int(linie)
    coloana = int(coloana)
    tabla = Joc(linie, coloana)
    print(str(tabla))
