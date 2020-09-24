
from colorama import Fore

misura_onda = 0


def misura_func():
    global misura_onda

    while True:
        try:
            misura_onda = int(input('[>] taschini vuoti tra ganci'.ljust(29, " "))) + 1
            if (misura_onda > 16) or (misura_onda < 2):
                print(Fore.LIGHTRED_EX)
                print("[!] numero taschini non valido!..")
                print(Fore.LIGHTGREEN_EX)
            else:
                break

        except ValueError:
            print(Fore.LIGHTRED_EX)
            print("[!] i dati inseriti non sono validi!\n[!] Riprova!\n")
            print(Fore.LIGHTGREEN_EX)


misura_func()
