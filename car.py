
from colorama import *
LINE = '_' * 50 + '\n'
"""
module doc
"""


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
    nodi="high" #puo essere "high", "low", "node"
    ):
    
    # distanza tra taschini
    dist_task = 52 / 29
    numero_ganci = 0
    
    final_result = [0, 0, 0, 0] # [binario, stoffa, numero_ganci, numero_nodi_da_fare]
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


    # [binario, stoffa, numero_ganci, numero_nodi_da_fare]
    # se la misura calcolata e` uguale alla misura iniziale
    # ritorna la misura
    if misura_bin == presunta_misura_bin:
        print("e uguale")
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)

    if nodi == "high":
        misura_bin += (passo * 2)
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)

    if nodi == "low":
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)

    if nodi == "node":
        if misura_bin < presunta_misura_bin:
            misura_bin += (passo * 2)
        final_result[0] = presunta_misura_bin if binary_type == 1 else presunta_misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        # final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)\
        # if binary_type == 1 else round(dist_task * (taschini_vuoti + 1), 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)
        final_result[3] = calcolo_nodi(misura_bin, passo, larghezza_massima_binario, presunta_misura_bin)

    return final_result


def print_ond(mis_ef, stoff, spaz_ganc, nodi):

    s = (
        f"{LINE}\n"
        f"{'binario'.ljust(27, ' ')}{mis_ef}\n"
        f"{'stoffa'.ljust(27, ' ')}{stoff}\n"
        f"{'spazio tra ganci'.ljust(27, ' ')}{spaz_ganc}\n"
        )
    s= s + f'{"numero nodi".ljust(27, " ")}{nodi}\n' if nodi > 0 else s
    s = s +LINE
    print(s)
    return ''




def ond(presunta_misura_bin, passo,  taschini_vuoti, binary_type):
    """
    calcoli per la fettuccia da 7 cm
    """
    print(LINE)
    print("S I N G O L O".center(50, " ") if binary_type == 1 else print("D O P P I O".center(50, " ")))
    misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "low")
    print_ond(misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi)
    misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "high")
    print_ond(misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi)
    misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "node")
    print("  N O D I  ".center(50, "*"))
    print_ond(misura_effettiva_binario, stoffa, spazio_tra_ganci, nodi)


if __name__ == "__main__":
    ond(387, 8, 7, 2)
    print()

