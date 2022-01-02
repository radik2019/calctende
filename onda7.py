
from colorama import *
import os
import sys, json
from setup_data import *

LARGE = 40
LINE = Fore.RED + ('_' * LARGE) + Fore.LIGHTYELLOW_EX +'\n' 
"""
module doc
"""


def read_proportion(flag: int = 0 )->list:
    """scelta del tipo di fettuccia"""
    lst = os.listdir()

    if "setup_data.json" in lst:
        numb = json_read("setup_data.json")
        return numb['onda'][flag]
    else:
        json_write("setup_data.json", dct)
        read_proportion(flag)


def binar():
    tipo_binario = input("[?] binario a 1 telo o 2? [1 / 2]: ")
    if tipo_binario == '2' or tipo_binario == '1':
        return int(tipo_binario)
    else:
        print("[!] inserisci '1' o '2'. indica se l'apertura e' laterale o centrale")
        return binar()


def calcolo_nodi(misura_bin, passo, larghezza_massima_binario, presunta_misura_bin):
    misura_bin += (passo * 2)
    da_dividere_per_nodi = larghezza_massima_binario - presunta_misura_bin
    numero_nodi = int(da_dividere_per_nodi / 0.75)
    return numero_nodi


def calcolo_ond(presunta_misura_bin,
    passo,
    taschini_vuoti, #numero di taschini vuoti tra i ganci
    binary_type = 1,
    nodi="high", #puo essere "high", "low", "node"
    fettuccia = 0
    ):
    
    # distanza tra taschini
    aa, ss = read_proportion(fettuccia)
    dist_task = aa / ss

    numero_ganci = 0
    
    final_result = [0, 0, 0, 0, 0] # [binario, stoffa, distanza_tra_taschini, numero_nodi_da_fare, numero_ganci]
    if binary_type == 1:
        pass
    else:
        presunta_misura_bin /= 2

    # calcolo del numero degli spazi tra gamci
    spazi_tra_ganci = presunta_misura_bin // passo
    if spazi_tra_ganci % 2 == 0:
        spazi_tra_ganci -= 1
    misura_bin = spazi_tra_ganci * passo
    # print("misura binario - ", misura_bin)

    larghezza_massima_binario = misura_bin + (passo * 2)

    if nodi == "high":
        misura_bin += (passo * 2)
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)
        final_result[4] = (misura_bin / passo) + 1 if binary_type == 1 else ((misura_bin / passo) + 1) * 2

    if nodi == "low":
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)
        final_result[4] = (misura_bin / passo) + 1 if binary_type == 1 else ((misura_bin / passo) + 1) * 2

    if nodi == "node":
        if misura_bin < presunta_misura_bin:
            misura_bin += (passo * 2)
        final_result[0] = presunta_misura_bin if binary_type == 1 else presunta_misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2

        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)
        final_result[3] = calcolo_nodi(misura_bin, passo, larghezza_massima_binario, presunta_misura_bin)
        final_result[4] = (misura_bin / passo) + 1 if binary_type == 1 else ((misura_bin / passo) + 1) * 2
    return final_result


def print_ond(mis_ef, stoff, spaz_ganc, nodi, ganci, binary_type):
    dct = json_read("setup_data.json")
    prezzo = (dct["prezzo_onda"] * (stoff /100))

    if binary_type == 2:
        prezzo += (dct["orli"] * 4)
    if binary_type == 1:
        prezzo += (dct["orli"] * 2)

    s = (
        Fore.LIGHTYELLOW_EX + f"{LINE}\n"
        f"{'binario'.ljust(27, ' ')}{mis_ef}\n"
        f"{'stoffa'.ljust(27, ' ')}{stoff}\n"
        f"{'numero ganci'.ljust(27, ' ')}{ganci}\n"
        f"{'spazio tra ganci'.ljust(27, ' ')}{spaz_ganc}\n"
        f"{'costo'.ljust(27, ' ')}{round(prezzo, 2)} euro\n"
        )
    s= s + f'{"numero nodi".ljust(27, " ")}{nodi}\n' if nodi > 0 else s
    s = s + LINE
    print(s)
    return ''


def ond(presunta_misura_bin, passo,  taschini_vuoti, binary_type, fettuccia):
    """
    calcoli per la fettuccia da 7 cm
    """
    print(LINE)
    misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1, ganci1 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "low", fettuccia)

    misura_effettiva_binario2, stoffa2, spazio_tra_ganci2, nodi2, ganci2 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "high", fettuccia)

    misura_effettiva_binario3, stoffa3, spazio_tra_ganci3, nodi3, ganci3 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "node", fettuccia)
    print(Fore.RED + "[!]" + Fore.YELLOW + " '7 GANCI VUOTI = 14.34 cm con la fettuccia da 7 cm" + Fore.LIGHTGREEN_EX)
    print(Fore.RED + "[!]" + Fore.YELLOW + " '3 GANCI VUOTI = 14.46 cm con la fettuccia da 9 cm" + Fore.LIGHTGREEN_EX)
    print("S I N G O L O".center(LARGE, " ") if binary_type == 1 else "D O P P I O".center(LARGE, " "))
    if misura_effettiva_binario1 == presunta_misura_bin:
        print_ond(misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1, ganci1, binary_type)
    else:	
        print_ond(misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1, ganci1, binary_type)
        print_ond(misura_effettiva_binario2, stoffa2, spazio_tra_ganci2, nodi2, ganci2, binary_type)
        print("  N O D I  ".center(LARGE, "*"))
        print_ond(misura_effettiva_binario3, stoffa3, spazio_tra_ganci3, nodi3, ganci3, binary_type)
        print("[!] nel prezzo sono inclusi gli orli")
    return

if __name__ == "__main__":
    ond(298, 8, 7, 1, 0)
    ond(298, 8, 7, 2, 0)
    print()




