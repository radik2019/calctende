import itertools
import time
from onda import *
from onda7 import *


def logo():
    lst2 = """
    _________        .__               __                     .___
    \_   ___ \_____  |  |   ____     _/  |_  ____   ____    __| _/
    /    \  \/\__  \ |  | _/ ___\    \   __\/ __ \ /    \  / __ | 
    \     \____/ __ \|  |_\  \___     |  | \  ___/|   |  \/ /_/ | 
     \______  (____  /____/\___  >____|__|  \___  >___|  /\____ | 
            \/     \/          \/_____/         \/     \/      \/ 
    
    """
    lst2 = lst2.split("\n")

    for i in lst2:
        print(i)
        time.sleep(0.07)


def help():
    lst = """

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
    print(lst)


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


def prop():
    def string_to_list(s):
        lst = s.split()
        try:

            lst = [float(lst[i]) for i in range(len(lst))]
        except ValueError:
            return ('deve contenere solo numeri naturali '
                    'e razionali usando il punto al posto della virgola '
                    )
        return lst

    def prop_n(lst, n):
        a = 0
        ls = []
        for i in range(len(lst) + 1):
            ab = itertools.combinations(lst, i)
            for k in ab:
                if sum(k) > a and sum(k) <= n:
                    a = sum(k)
                    ls = k
                else:
                    pass
        return ls

    index_n = 1

    def choice_list(sottopezzi, pezzi, index_n):

        for i in pezzi:
            lst.append(prop_n(sottopezzi, i))
            sum_list.append(i - sum(prop_n(sottopezzi, i)))
        # print(sum_list)
        ind = sum_list.index(min(sum_list))

        df[f'{index_n}) {pezzi.pop(ind)}'] = lst[ind]

        for k in lst[ind]:
            sottopezzi.remove(k)
        return

    sottopezzi = string_to_list(input('inserisci i pezzi pronti:\t'))
    pezzi = string_to_list(input('inserisci i pezzi da dividere:\t'))
    df = {}
    while len(sottopezzi) > 0 and len(pezzi) > 0:
        lst = []
        sum_list = []
        choice_list(sottopezzi, pezzi, index_n)
        index_n += 1
    resti = []
    for i in df:
        print('_' * 50)
        # print(f'{i} -- {df[i]}\nresto -- {i - sum(df[i])}')
        print(f'{i} -- {sum(df[i])} = {df[i]}')
        if (float(i[3:]) - sum(df[i])) != 0:
            resti.append(float(i[3:]) - sum(df[i]))

    print('_' * 50)
    print(f'manca materiale per: {sottopezzi}')
    print(f'avanzano:            {resti}')
    # print(f'sono avanzati        {sum(pezzi)}')
    return ' '


# 2.82 23.75 45.45 2.65 4.12 76.93 2.56 5.78 34.56 65.92 12.83 32.67 45.39 29.67 27.73 24.52 16.91 18.65
# 234.45 345.67 178.89


def pg_input(

):
    m_tend = float(input('misura tenda:'.ljust(15, ' ')))
    m_stoff = float(input('stoffa'.ljust(15, ' ')))
    piega = float(input('piega:'.ljust(15, ' ')))
    piega_den = float(input('piega dentro:'.ljust(15, ' ')))
    space = float(input('spazio pieghe:'.ljust(15, ' ')))
    return [m_tend, m_stoff, piega, piega_den, space]


def pg():
    m_tend, m_stoff, piega, piega_den, space = pg_input()

    coef = (m_tend + space) // (space + piega)
    piega = ((m_tend + space) / coef) - space
    interval = ((m_stoff - (piega_den * 2) - m_tend) / (coef - 1)) / 2
    print(
        f"{'_' * 40}\n"
        f"{'piega'.ljust(15, ' ')}{round(piega, 1)}\n"
        f"{'spazio'.ljust(15, ' ')}{round(space, 1)}\n"
        f"{'intervallo'.ljust(15, ' ')}{round(interval, 1)}\n"
        f"{'_' * 40}\n"
    )

    i = 0
    while i < m_stoff:
        i += piega
        print('piega'.ljust(14, " "), round(i, 1))
        i += interval
        print("interval".ljust(14, " "), round(i, 1))
        i += space
        print("spazio".ljust(14, " "), round(i, 1))
        i += interval
        print("intervallo ".ljust(14, " "), round(i, 1), end="\n\n")
    print(f"sarebbe perfetta con questa metratura di stoffa "
          f""
          f"{round((piega * (coef * 2) + ((coef - 1) * space)) + (piega_den * 2), 1)}")


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
                pg()

            elif dom == "help":
                help()
            else:
                print('[!] commando non trovato...')
