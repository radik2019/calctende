

def onda_input():

    def pass_func():
        nonlocal passo
        try:
            passo = int(input('[>] passo "8" o "6"\t\t\t'))
        except ValueError:

            pass_func()

        try:
            while passo != 8 and passo != 6:
                # if passo != 8 and passo != 6:
                print("[!] il passo deve essere da 6 o da 8!")
                passo = int(input('[>] passo "8" o "6"\t\t\t'))
        except ValueError:
            print("[!] i dati inseriti non sono validi!\n[!] Riprova!\n\n")
            pass_func()

    def misura_func():
        nonlocal misura_onda
        try:
            misura_onda = int(input('[>] taschini vuoti tra ganci\t')) + 1
        except ValueError:
            print("[!] deve contenere solo numeri!..")
            misura_func()

        try:
            while (misura_onda > 16) or (misura_onda < 2):
                print("[!] numero taschini non valido!..")
                misura_onda = int(input('[>] taschini vuoti tra ganci\t')) + 1
        except ValueError:
            print("[!] i dati inseriti non sono validi!\n[!] Riprova!\n\n")
            misura_func()

    def binario_func():
        nonlocal binario
        try:
            binario = float(input('[>] misura del binario\t\t'))
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            binario_func()

        try:
            while binario < 100:
                print("[!] binario troppo piccolo")
                binario = float(input('[>] misura del binario\t\t'))
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            binario_func()

    passo = 0
    pass_func()

    misura_onda = 0
    misura_func()

    binario = 0
    binario_func()

    return [binario, passo, misura_onda]


def onda(binario, passo, misura_onda):

    mis_task = 126.5 / 35  # misura tra i taschini

    mis_bin = (binario // passo) * passo
    if mis_bin % 2 != 0:
        mis_bin += passo
    if mis_bin < binario:
        mis_bin2 = mis_bin + (2 * passo)
    else:
        mis_bin2 = mis_bin - (2 * passo)
    ganci1 = (mis_bin // passo) + 1
    ganci2 = (mis_bin2 // passo) + 1

    stoffa1 = (mis_bin // passo) * mis_task * misura_onda
    stoffa2 = (mis_bin2 // passo) * mis_task * misura_onda
    print(f"numero taschini   {misura_onda}")
    print(
        '\n'
        f'{"-" * 48}\n'
        f'binario\t\t\t{mis_bin}\n'
        f'numero ganci \t{ganci1}\n'
        f'misura stoffa\t{round(stoffa1, 2)}\n'
        f'{"-" * 48}\n'
        '          *OPPURE*\n'
        f'{"-" * 48}\n'
        f'binario\t\t\t{mis_bin2}\n'
        f'numero ganci \t{ganci2}\n'
        f'misura stoffa\t{round(stoffa2, 2)}\n'
        f'{"-" * 48}\n'
        f'spazio tra ganci: {round((mis_task * misura_onda), 2)}\n'
        f"numero taschini   {misura_onda - 1}\n"
        f'\n'

        f'{"-" * 48}\n'
        f' _________________________________________\n'
        f'|                                         |\n'
        f'|   le misure non includono gli orli e    |\n'
        f'|  la misura della stoffa piegata dentro  |\n'
        f'|_________________________________________|\n'

    )
