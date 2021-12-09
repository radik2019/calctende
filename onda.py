from colorama import *

def onda_input():
    def binar():
        tipo_binario = input("[>] binario a 1 telo o 2? [1 / 2]: ")
        if tipo_binario == '2' or tipo_binario == '1':
            return int(tipo_binario)
        else:
            print("[!] inserisci '1' o '2'. indica se l'apertura e' laterale o centrale")
            return binar()

    def pass_func():
        """ input per onda"""
        nonlocal passo

        try:
            while True:
                passo = int(input('[>] passo "8" o "6'.ljust(29, " ")))
                if passo != 8 and passo != 6:
                    print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX +" il passo deve essere da 6 o da 8!")
                else:
                    break

        except ValueError:
            print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX +" i dati inseriti non sono validi!")
            pass_func()

    def misura_func():
        nonlocal misura_onda

        while True:
            try:
                misura_onda = int(input('[>] taschini vuoti tra ganci  '.ljust(29, " ")))
                if (misura_onda > 16) or (misura_onda < 2):

                    print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX + " numero taschini non valido!..")

                else:
                    break

            except ValueError:
                print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX + " i dati inseriti non sono validi!\n[!] Riprova!\n")

    def binario_func():
        nonlocal binario
        try:
            binario = float(input('[>] misura del binario'.ljust(29, " ")))
        except ValueError:
            print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX +" i dati inseriti non sono validi!")

            binario_func()

        try:
            while binario < 100:
                print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX +"[!] binario troppo piccolo")

                binario = float(input('[>] misura del binario'.ljust(29, " ")))
        except ValueError:
            print(Fore.RED + "[!]" + Fore.LIGHTGREEN_EX +" i dati inseriti non sono validi!")
            binario_func()

    def input_fettuccia():
        tipo_fettuccia = input("[>] fettuccia da 7 cm o da 9 cm? [7 / 9]: ")
        if tipo_fettuccia == '7' or tipo_fettuccia == '9':
            if tipo_fettuccia == '7':
                return 0
            else:
                return 1
            return int(tipo_fettuccia)
        else:
            print("[!] inserisci '7' o '9'. indica il tipo di fettuccia")
            return input_fettuccia()                  

    passo = 0
    pass_func()

    misura_onda = 0
    misura_func()

    binario = 0
    binario_func()
    binar_type = binar()
    fettuccia = input_fettuccia()

    return [binario, passo, misura_onda, binar_type, fettuccia]


# def onda(binario, passo, misura_onda):

#     mis_task = 126.5 / 35  # misura tra i taschini

#     mis_bin = (binario // passo) * passo
#     if mis_bin % 2 != 0:
#         mis_bin += passo
#     if mis_bin < binario:
#         mis_bin2 = mis_bin + (2 * passo)
#     else:
#         mis_bin2 = mis_bin - (2 * passo)
#     ganci1 = (mis_bin // passo) + 1
#     ganci2 = (mis_bin2 // passo) + 1

#     stoffa1 = (mis_bin // passo) * mis_task * misura_onda
#     stoffa2 = (mis_bin2 // passo) * mis_task * misura_onda
#     print(f"numero taschini   {misura_onda}")
#     print(
#         '\n'
#         f'{"-" * 48}\n'
#         f'binario\t\t\t{mis_bin}\n'
#         f'numero ganci \t{ganci1}\n'
#         f'misura stoffa\t{round(stoffa1, 2)}\n'
#         f'{"-" * 48}\n'
#         '          *OPPURE*\n'
#         f'{"-" * 48}\n'
#         f'binario\t\t\t{mis_bin2}\n'
#         f'numero ganci \t{ganci2}\n'
#         f'misura stoffa\t{round(stoffa2, 2)}\n'
#         f'{"-" * 48}\n'
#         f'spazio tra ganci: {round((mis_task * misura_onda), 2)}\n'
#         f"numero taschini   {misura_onda - 1}\n"
#         f'\n'

#         f'{"-" * 48}\n'
#         f' _________________________________________\n'
#         f'|                                         |\n'
#         f'|   le misure non includono gli orli e    |\n'
#         f'|  la misura della stoffa piegata dentro  |\n'
#         f'|_________________________________________|\n'

#     )
