import getopt
import sys
# functie ajutatoare pentru a prelua parametrii din linia de comanda, in functie de un anumit format dat
def get_arguments(argv):
    input_lin = ''
    input_col = ''
    input_jucator = ''
    input_dificultate = ''
    input_alg = ''
    input_gui = ''
    print(
        "\nBine ati venit in jocul Obstruction. Pentru a incepe, trebuie introduse nr de linii, nr de coloane, dintre care cel putin unul sa fie numar par.")
    print(
        "\nDe asemenea, daca doriti sa jucati cu X sau cu 0,dificultatea(incepator, mediu,avansat), algoritmul dorit(min-max sau alpha-beta) si daca doriti sa jucati cu ajutorul unei interfete grafice sau nu(se va raspunde cu DA sau NU")

    try:
        # se iau in calcul si denumirea argumentelor, nu doar inputul pe care il vreau
        if len(argv) != 12:
            print('Inputul trebuie sa fie de forma:')
            print('obstruction.py -l <nr_lin> -c <nr_col> -j <jucator> -d <dificultate> -a <algoritm> -i <gui>')
            sys.exit(2)

        opts, args = getopt.getopt(argv, "hl:c:j:d:a:i", ["lin", "col", "jucator", "dificultate", "alg", "gui"])
    except getopt.GetoptError:
        print("Inputul nu a fost introdus corect:")
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