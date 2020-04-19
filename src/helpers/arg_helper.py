import getopt
import sys

def get_arguments(argv):
    input_lin = ''
    input_col = ''
    input_jucator = ''
    input_dificultate = ''
    input_alg = ''
    input_gui = ''

    try:
        # se iau in calcul si denumirea argumentelor, nu doar inputul pe care il vreau
        if len(argv) != 12:
            print('Inputul trebuie sa fie de forma:')
            print('obstruction.py -l <nr_lin> -c <nr_col> -j <jucator> -d <dificultate> -a <algoritm> -i <gui>')
            sys.exit(2)

        opts, args = getopt.getopt(argv, "hl:c:j:d:a:i", ["lin", "col", "jucator", "dificultate", "alg", "gui"])
    except getopt.GetoptError:
        print("Inputul nu a fost introduc corect:")
        print('obstruction.py -l <nr_lin> -c <nr_col> -j <jucator> -d <dificultate> -a <algoritm> -i <gui>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('obstruction.py -l <nr_lin> -c <nr_col> -j <jucator> -d <dificultate> -a <algoritm> -i <gui>')
            sys.exit()
        elif opt in ('-l', '--lin'):
            input_lin = arg
        elif opt in ('-c', '--col'):
            input_col = arg
        elif opt in ('-j', '--jucator'):
            input_jucator = arg
        elif opt in ('-d', '--dificultate'):
            input_dificultate = arg
        elif opt in ('-a', '--algoritm'):
            input_alg = arg
        elif opt in ('-i', '--gui'):
            input_gui = arg
    return input_lin, input_col, input_jucator, input_dificultate, input_alg, input_gui