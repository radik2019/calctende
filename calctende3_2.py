#!/usr/bin/python3


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
import os, sys

from colorama import *

from pretyPrint import *

print(Style.BRIGHT)
alert = f'[{chr(10071)}]'


def logo():
    lst2 = """
╔═══╗     ╔╗      ╔════╗          ╔╗
║╔═╗║     ║║      ║╔╗╔╗║          ║║
║║ ╚╝╔══╗ ║║ ╔══╗ ╚╝║║╚╝╔══╗╔═╗ ╔═╝║
║║ ╔╗╚ ╗║ ║║ ║╔═╝   ║║  ║╔╗║║╔╗╗║╔╗║
║╚═╝║║╚╝╚╗║╚╗║╚═╗  ╔╝╚╗ ║║═╣║║║║║╚╝║
╚═══╝╚═══╝╚═╝╚══╝  ╚══╝ ╚══╝╚╝╚╝╚══╝
    """

    lst2 = lst2.split("\n")

    for i in lst2:
        print(Fore.CYAN, i)
        time.sleep(0.04)


def data_input(list_ask):
    def list_of_measures(s):
        try:
            question = input(s.ljust(22, ' '))
            if question.lower() == "stop":
                return None
            question = float(question)
            return question
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            return list_of_measures(s)

    list_mis = []
    for ask in list_ask:
        data = list_of_measures(ask)
        if not data:
            return None
        list_mis.append(data)
    return list_mis


def check(lst, func):
    misure = data_input(lst)
    if misure:
        return func(misure)
    return


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

def check_app(obj):
    try:
        obj()()
    except TypeError:
        pass
if __name__ == "__main__":
    if sys.platform == "linux":
        CLEAR_SCREEN = "clear"
    elif sys.platform == "win32":
        CLEAR_SCREEN = "cls"
        init(convert=True)
    dom = 23
    os.system(CLEAR_SCREEN)
    logo()
    while dom != 'stop':
        lista_piega_fissa = ['piega fissa', 'piega']
        st_piega = ['stp', 'stoffa per piega fissa']
        proporzioni = ['prop', 'proporzioni']
        ondal = ['tende a onda', 'onda']
        onda7 = ['onda', 'onda7', 'onda 7cm', 'fettuccia 7 cm', 'tende a onda', 'onda']
        nastr = ['nastro', 'nastro_barra', 'nastrobarra', 'nastro barra']

        dom = 23
        while dom != 'stop':
            print(Fore.LIGHTCYAN_EX)
            dom = input('[>]\t').lower()
            print(Fore.LIGHTGREEN_EX)

            if dom in lista_piega_fissa:
                check_app(PiegaFissa)
            elif dom == "ptube":
                check_app(PiegaTubolare)


            elif dom in nastr:
                nastro_barra()
            elif dom in proporzioni:
                prop()
            elif dom in st_piega:
                check_app(StoffaPiegaFissa)

            elif dom in onda7:

                print(
                    Fore.RED + "[!]" + Fore.YELLOW + " '7 GANCI VUOTI = 14.34 cm con la fettuccia da 7 cm" + Fore.LIGHTGREEN_EX)
                print(
                    Fore.RED + "[!]" + Fore.YELLOW + " '3 GANCI VUOTI = 14.46 cm con la fettuccia da 9 cm" + Fore.LIGHTGREEN_EX)

                lstond = onda_input()
                ond(lstond[0], lstond[1], lstond[2], lstond[3], lstond[4])






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
            elif dom in ["cls", "clear", "erase"]:
                os.system(CLEAR_SCREEN)
            else:
                # print(Fore.LIGHTRED_EX)
                print(alert + ' commando non trovato...\n'
                              f'{alert} [ help ] per la lista dei comandi\n'
                              '[' + chr(10071) + '] [ stop ] per fermare il programma')
                print(Fore.LIGHTCYAN_EX)
