import itertools
import time
from onda import *
from onda7 import *
from proportion import *
from piega_tubolare import *


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


def help():
    help_string = """

		"stp" ---- calcolo della stoffa per la piega fissa'

		"onda" --- tende a onda  

		"onda7"--- tende a onda con fettuccia da 7 cm  

		"piega"--- piega fissa 

		"nastro"-- nastro barra 

		"stop"---- chiude il programma 

		"prop"---- taglio senza spreco scrivere i numeri divisi da spazio, i 
			num non interi vanno scritti con il punto esem.: 2.3 4.67 etc   

		"ptube"--- piega a tubo 

		
	"""
    print(help_string)


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


# 2.82 23.75 45.45 2.65 4.12 76.93 2.56 5.78 34.56 65.92 12.83 32.67 45.39 29.67 27.73 24.52 16.91 18.65
# 234.45 345.67 178.89


# ##########################################################


def pf_input():
    piega_aprossimata = float(input("m. piega:".ljust(12, ' ')))
    piega_dentro = float(input("m. dentro:".ljust(12, ' ')))
    misura_tenda = float(input("m. tenda:".ljust(12, ' ')))
    misura_stoffa = float(input("m. stoffa:".ljust(12, ' ')))
    print('_' * 20)
    return [piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa]


def pf(piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa):
    coef = ((piega_dentro * 2) + misura_tenda)
    while misura_stoffa <= coef:
        print('la stoffa non puo essere piu piccola della tenda')
        misura_stoffa = float(input("m. stoffa: \t"))
    numero_pieghe = (misura_tenda // piega_aprossimata)  # numero pieghe
    misura_piega = (misura_tenda / numero_pieghe)  # dimensione pieghe
    intervallo_piega = (misura_stoffa - misura_tenda - (piega_dentro * 2)) / \
                       (numero_pieghe - 1)  # intrervallo tra pieghe
    print(
        '\n'
        f'{"piega".ljust(12, " ")}{str(round(misura_piega, 1)).rjust(6, " ")}\n'
        f'{"intervallo".ljust(12, " ")}{str(round(intervallo_piega, 1)).rjust(6, " ")}\n'
        f'{"stoffa".ljust(12, " ")}{str(round(misura_stoffa, 1)).rjust(6, " ")}\n'
        f'{"tenda".ljust(12, " ")}{str(round(misura_tenda, 1)).rjust(6, " ")}\n'
        f'\n'
        f'{"C A L C O L I".rjust(16, " ")}'
    )

    i = (misura_piega + intervallo_piega)
    print('piega\t\t', (round(misura_piega, 1)))
    print('intervallo\t', (round(i, 1)))
    while i < 250:
        i = i + misura_piega
        print('piega\t\t', (round(i, 1)))
        i = i + intervallo_piega
        print('intervallo\t', (round(i, 1)))
    print()


###############################################################


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
                lstpf = pf_input()
                pf(lstpf[0], lstpf[1], lstpf[2], lstpf[3])

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
                pg(pg_input())

            elif dom == "help":
                help()
            else:
                print('[!] commando non trovato...')
