
import time
from onda import *
from onda7 import *
from proportion import *
from piega_tubolare import *
from piega_fissa import *
from help import *
from stoffa_piegafissa import *
from taglio_coeficiente import *
import preventivo
import tenda_romana


from colorama import *

from pretyPrint import *


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
        print(Fore.CYAN, i)
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
            print(Fore.LIGHTCYAN_EX)
            dom = input('[>]\t').lower()
            print(Fore.LIGHTGREEN_EX)
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
                stoffa_per_piega_fissa(data_input(list_ask_stoffa))

            elif dom in onda7:
                lstond = onda_input()
                ond(lstond[0], lstond[1], lstond[2])

            elif dom == "ptube":
                pg(data_input(list_ask_tub))

            elif dom == "help":
                help()

            elif dom in ["coeficente", "coef"]:
                list_ask_coef = input_coef()
                coef(list_ask_coef[0], list_ask_coef[1], list_ask_coef[2])


            elif dom == "stop":
                print("[!] a presto!\n\n")
            elif dom in ["preventivo", "prev"]:
                preventivo.start()
            elif dom in ["tenda romana", "romana", "steccata", "tenda steccata"]:
                tenda_romana.t_romana(data_input(["altezza tenda", 'fettuccia', "basso", "bacchette"]))
            else:
                print(Fore.LIGHTRED_EX)
                print('[!] commando non trovato...\n'
                    '[!] [ help ] per la lista dei comandi\n'
                    '[!] [ stop ] per fermare il programma')
                print(Fore.LIGHTCYAN_EX)
