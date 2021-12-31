
from data_input import *

list_ask_stoffa = ['tenda:', 'piega:', 'piega dentro:']


def stoffa_per_piega_fissa(list_ask):
    """
    si calcola la stoffa per la piega fissa.
    nel risultato si include anche la piega dentro
    :return: quanta stoffa devi avere
    """

    tenda, piega, piega_dentro = list_ask
    numero_di_pieghe: int = tenda // piega
    piega = tenda / numero_di_pieghe
    print('_' * 50)
    print(f'stoffa:\t{((piega * numero_di_pieghe) + ((piega * 2) * (numero_di_pieghe - 1))) + (piega_dentro * 2)}')
    print(f'piega:\t{piega}')
    print('_' * 50)

# stoffa_per_piega_fissa([156, 10, 12])


class StoffaPiegaFissa(DataInput):
    def __init__(self, *args):
        super().__init__()
        if all(args) and len(args) == 3:
            if max(args[1], args[2]) < args[0]:
                self.tenda = args[0]
                self.piega = args[1]
                self.piega_dentro = args[2]
                self.numero_di_pieghe: int = self.tenda // self.piega
                self.piega = self.tenda / self.numero_di_pieghe
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")
        else:
            self.readyToInput = self.data_input()
            if max(self.readyToInput[1], self.readyToInput[2]) < self.readyToInput[0]:
                self.tenda, self.piega, self.piega_dentro = self.readyToInput
                self.numero_di_pieghe: int = self.tenda // self.piega
                self.piega = self.tenda / self.numero_di_pieghe
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")

    def calculated_measures(self):
        stoffa = ((self.piega * self.numero_di_pieghe) + ((self.piega * 2) * (self.numero_di_pieghe - 1))) + (self.piega_dentro * 2)
        return stoffa

    def output(self):
        print('_' * 50)
        print(f'stoffa:\t{self.calculated_measures()}')
        print(f'piega:\t{self.piega}')
        print('_' * 50)

    def __call__(self):
        try:
            self.output()
        except TypeError:
            pass

if __name__ == "__main__":
    StoffaPiegaFissa()()