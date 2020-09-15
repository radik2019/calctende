import itertools
import time
from onda import *
from onda7 import *
from proportion import *
from piega_tubolare import *
from piega_fissa import *
from help import *


def logo():
    lst2 = """
╔═══╗     ╔╗         ╔════╗          ╔╗
║╔═╗║     ║║         ║╔╗╔╗║          ║║
║║ ╚╝╔══╗ ║║ ╔══╗    ╚╝║║╚╝╔══╗╔═╗ ╔═╝║
║║ ╔╗╚ ╗║ ║║ ║╔═╝      ║║  ║╔╗║║╔╗╗║╔╗║
║╚═╝║║╚╝╚╗║╚╗║╚═╗     ╔╝╚╗ ║║═╣║║║║║╚╝║
╚═══╝╚═══╝╚═╝╚══╝     ╚══╝ ╚══╝╚╝╚╝╚══╝

    """

    lst2 = lst2.split("\n")

    for i in lst2:
        print(i)
        time.sleep(0.07)


def data_input(list_ask):
    def list_of_measures(s):
        try:
            question = float(input(s.ljust(22, ' ')))
            return question
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            return list_of_measures(s)
    list_mis = []
    for ask in list_ask:
        list_mis.append(list_of_measures(ask))
    return list_mis



def onda_nod(misura_bin, passo, taschini_vuoti):
    # taschini_vuoti = int(input('taschini vuoti tra ganci:'.ljust(27, ' ')))
    # misura_bin = float(input('misura binario:'.ljust(27, ' ')))
    # passo = int(input('passo "8" o "6":'.ljust(27, ' ')))
    numero_ganci = misura_bin // passo
    if numero_ganci % 2 == 0:
        numero_ganci += passo
    filo = numero_ganci * passo
    print(numero_ganci)
    print(filo)


def stoffa_per_piega_fissa():
    '''
	si calcola la stoffa per la piega fissa.
	nel risultato si include anche la piega dentro
	:return: quanta stoffa devi avere
	'''
    tenda = float(input('tenda:\t\t'))
    piega = int(input('piega:\t\t'))
    piega_dentro = float(input('piega dentro:\t'))
    sa = tenda // piega
    coef = tenda / sa
    print(f'stoffa:\t{((coef * sa) + ((coef * 2) * (sa - 1))) + (piega_dentro * 2)}')
    print(f'piega:\t{coef}')


def nastro_barra():
    fettuccia = input('da dove viene la stoffa?\t')
    fettuccia = fettuccia.lower()
    if fettuccia == 'micheletti':
        stoffa = float(input(' misura bastone\t'))
        stoffa = stoffa * 1.5
        coef_td = 233 / 11
        stoffa_gius = stoffa // coef_td
        passante = 3.5
        print("=" * 50)
        print('da aggiungere la piega dentro')
        print()
        print(stoffa_gius * coef_td + passante)
        print("numero di onde = {} ".format(int(stoffa_gius)))
        print("=" * 50)
    else:
        pass
    return ' '


###############################################################

if __name__ == "__main__":
    dom = 23
    logo()
    while dom != 'stop':
        tendel = ['piega fissa', 'piega']
        st_piega = ['stp', 'stoffa per piega fissa']
        proporzioni = ['prop', 'proporzioni']
        ondal = ['tende a onda', 'onda']
        onda7 = ['onda7', 'onda 7cm', 'fettuccia 7 cm']
        nastr = ['nastro', 'nastro_barra', 'nastrobarra', 'nastro barra']
        dom = 23
        while dom != 'stop':
            dom = input('[>]\t').lower()

            if dom in tendel:

                pf(data_input(list_ask_piega))

            elif dom in ondal:
                lstonda = onda_input()
                onda(lstonda[0], lstonda[1], lstonda[2])

            elif dom in nastr:
                nastro_barra()
            elif dom in proporzioni:
                prop()
            elif dom in st_piega:
                stoffa_per_piega_fissa()

            elif dom in onda7:
                lstond = onda_input()
                ond(lstond[0], lstond[1], lstond[2])

            elif dom == "ptube":
                pg(data_input(list_ask_tub))

            elif dom == "help":
                help()
            else:
                print('[!] commando non trovato...')
