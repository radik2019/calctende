from pretyPrint import *
from setup_data import *
import click
from data_input import DataInput


list_ask_piega = [
    "m. piega:", "m. dentro:", "m. tenda:", "m. stoffa:"
]

class PiegaFissa(DataInput):

    ASSE_DA_STIRO = 121
    PRINTED_WIDTH = 30
    APP_NAME = ' '.join(list("PIEGA FISSA")).center(PRINTED_WIDTH, ' ')

    def __init__(self, piega_aprossimata=None, m_dentro=None, misura_tenda=None, misura_stoffa=None):
        super().__init__()
        self.exitFlag = True
        if not all((piega_aprossimata, m_dentro, misura_tenda, misura_stoffa)):
            self.readyToInput = self.data_input()
            if self.readyToInput:
                self.piega_aprossimata, self.m_dentro, self.misura_tenda, self.misura_stoffa = self.readyToInput
            else:
                self.exitFlag = False
        else:
            self.piega_aprossimata = piega_aprossimata
            self.m_dentro = m_dentro
            self.misura_tenda = misura_tenda
            self.misura_stoffa = misura_stoffa

        if self.exitFlag:
            self.asseFlag = True
            self.listaMisurePronte = []
            self.asseDaStiroMisure = None
            self.set_piega()
            self.setNumeroPieghe()
            self.set_intervallo()
            self.setListaMisurePronte()
    def __call__(self):
        """

        @rtype: object
        return: None
        """
        self.printMisure()
        
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
        if self.exitFlag:
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
    PiegaFissa()()


    # pf([9, 12, 167, 378])
