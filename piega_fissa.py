from pretyPrint import *
from setup_data import *
import click


list_ask_piega = [
    "m. piega:", "m. dentro:", "m. tenda:", "m. stoffa:"
]

class DataInput:
    pass
class PiegaFissa(DataInput):

    ASSE_DA_STIRO = 121
    PRINTED_WIDTH = 30
    APP_NAME = ' '.join(list("PIEGA FISSA")).center(PRINTED_WIDTH, ' ')

    def __init__(self, piega_aprossimata, m_dentro, misura_tenda, misura_stoffa):
        self.asseFlag = True
        self.piega_aprossimata = piega_aprossimata
        self.m_dentro = m_dentro
        self.misura_tenda = misura_tenda
        self.misura_stoffa = misura_stoffa
        # self.coeficiente = ((self.m_dentro * 2) + self.misura_tenda)
        self.listaMisurePronte = []
        self.asseDaStiroMisure = None
        # return -> (misura piega, numero di pieghe)
        self.set_piega()
        self.setNumeroPieghe()
        self.set_intervallo()
        self.setListaMisurePronte()
        
    def set_piega(self) -> tuple:
        self.piega_effettiva = self.misura_tenda / (self.misura_tenda // self.piega_aprossimata)
    
    def setNumeroPieghe(self):
        self.numeroPieghe = self.misura_tenda / self.piega_effettiva

    def set_intervallo(self):
        stoffa_rimanente = self.misura_stoffa - ((self.m_dentro * 2) + self.misura_tenda)
        self.intervallo_piega = stoffa_rimanente / (self.numeroPieghe - 1)

    def setListaMisurePronte(self):
        asseFlag = True
        count = 0
        i = 0
        while i < (self.misura_stoffa - self.m_dentro * 2):
            i += self.piega_effettiva
            self.listaMisurePronte.append(round(i, 2))
            i += self.intervallo_piega
            self.listaMisurePronte.append(round(i, 2))
    
    def printInputData(self):
        print()
        print(click.style(self.__class__.APP_NAME, fg='bright_cyan'), end="\n\n")
        print(click.style(f"piega dentro   {self.m_dentro}", fg='yellow'))
        print(click.style(f"piega          {round(self.piega_effettiva, 2)}", fg='yellow'))
        print(click.style(f"misura tenda   {self.misura_tenda}", fg='yellow'))
        print(click.style(f"misura stoffa  {self.misura_stoffa}", fg='yellow'))
        print(click.style(f"numero pieghe  {int(self.numeroPieghe)}\n", fg='yellow'))
    
    def pricePrint(self):
        dct = json_read("setup_data.json")
        prezzo = dct["prezzo_piegafissa"] * (self.misura_stoffa / 100) + (dct["orli"] * 2)
        alert = click.style("[!]", fg="red", blink=True, bold=True)
        prezzo = click.style(f" prezzo inclusi gli orli  {prezzo}", fg="bright_yellow")
        
        click.echo(alert + prezzo)
        print()

    def printMisure(self):
        df = ' '.join(list("CALCOLI")).center(self.__class__.PRINTED_WIDTH, ' ')
        self.printInputData()
        print(click.style(df, fg="bright_cyan"), end='\n\n')
        for i in range(0, len(self.listaMisurePronte), 2):
            if self.asseFlag and (self.listaMisurePronte[i + 1] > self.__class__.ASSE_DA_STIRO):
                self.asseFlag = False
                print(click.style('*' * self.__class__.PRINTED_WIDTH, fg="bright_cyan"))

            print(click.style(f"piega        {self.listaMisurePronte[i]}", fg='bright_yellow'))
            print(f"intervallo   {self.listaMisurePronte[i + 1]}")
        print()
        self.pricePrint()




if __name__ == "__main__":
    p = PiegaFissa(9, 12, 167, 378)

    p.printMisure()
    # pf([9, 12, 167, 378])



# def pf(list_data, asse_da_stiro=121):

#     piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa = list_data

#     coef = ((piega_dentro * 2) + misura_tenda)
    
#     while misura_stoffa <= coef:
#         printAlert('[ ! ] la stoffa non puo essere piu piccola della tenda')
#         misura_stoffa = float(input("m. stoffa: \t"))
#     numero_pieghe = (misura_tenda // piega_aprossimata)  # numero pieghe
#     misura_piega = (misura_tenda / numero_pieghe)  # dimensione pieghe
#     intervallo_piega = (misura_stoffa - misura_tenda - (piega_dentro * 2)) / \
#                        (numero_pieghe - 1)  # intrervallo tra pieghe
#     print(
#         '\n'
#         f'{"piega".ljust(12, " ")}{str(round(misura_piega, 1)).rjust(6, " ")}\n'
#         f'{"intervallo".ljust(12, " ")}{str(round(intervallo_piega, 1)).rjust(6, " ")}\n'
#         f'{"stoffa".ljust(12, " ")}{str(round(misura_stoffa, 1)).rjust(6, " ")}\n'
#         f'{"tenda".ljust(12, " ")}{str(round(misura_tenda, 1)).rjust(6, " ")}\n'
#         f'\n'
#         f'{"C A L C O L I".rjust(16, " ")}'
#     )

#     i = (misura_piega + intervallo_piega)
#     print('piega\t\t', (round(misura_piega, 1)))
#     print('intervallo\t', (round(i, 1)))

#     asse_flag = True

#     while i < (misura_stoffa - piega_dentro * 2):

#         i = i + misura_piega
#         print('piega\t\t', (round(i, 1)))
#         i = i + intervallo_piega
#         print('intervallo\t', (round(i, 1)))

#         if asse_flag and asse_da_stiro > i > 90:

#             if (i + misura_piega + intervallo_piega) > asse_da_stiro:

#                 printAlert("*" * 22)
#                 asse_flag = False

#     dct = json_read("setup_data.json")
#     prezzo = dct["prezzo_piegafissa"] * (misura_stoffa / 100) + (dct["orli"] * 2)
#     print(Fore.RED + "[!]" + Fore.LIGHTYELLOW_EX + f"{' prezzo inclusi gli orli  '}{prezzo}")








































