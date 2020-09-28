
from pretyPrint import *

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


def data_input2():
    pass


def pf(list_data):
    piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa = list_data
    coef = ((piega_dentro * 2) + misura_tenda)
    while misura_stoffa <= coef:
        printAlert('la stoffa non puo essere piu piccola della tenda')
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

    asse_flag = True

    while i < (misura_stoffa - piega_dentro * 2):

        i = i + misura_piega
        print('piega\t\t', (round(i, 1)))
        i = i + intervallo_piega
        print('intervallo\t', (round(i, 1)))


        if asse_flag and 120 > i > 90:

            if (i + misura_piega + intervallo_piega) > 120:

                print("*" * 40)
                asse_flag = False



    print()


if __name__ == "__main__":
    list_ask_piega = [
        "m. piega:", "m. dentro:", "m. tenda:", "m. stoffa:"
    ]

    pf(data_input(list_ask_piega))
