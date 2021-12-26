
from data_input import *

list_ask_stoffa = ['tenda:', 'piega:', 'piega dentro:']


def stoffa_per_piega_fissa(list_ask):
    """
    si calcola la stoffa per la piega fissa.
    nel risultato si include anche la piega dentro
    :return: quanta stoffa devi avere
    """

    tenda, piega, piega_dentro = list_ask
    sa = tenda // piega
    coef = tenda / sa
    print('_' * 50)
    print(f'stoffa:\t{((coef * sa) + ((coef * 2) * (sa - 1))) + (piega_dentro * 2)}')
    print(f'piega:\t{coef}')
    print('_' * 50)


class StoffaPiegaFissa(DataInput):
    def __init__(self, *args):

        super().__init__()
        if all(args) and len(args) == 3:
            if max(args[1], args[2]) < args[0]:
                self.tenda = args[0]
                self.piega = args[1]
                self.piega_dentro = args[2]
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")
        else:
            self.readyToInput = self.data_input()
            if max(self.readyToInput[1], self.readyToInput[2]) < self.readyToInput[0]:
                self.tenda, self.piega, self.piega_dentro = self.readyToInput
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")

    def calculated_measures(self):
        pass

    def __print_header(self):
        pass

    def __print_body(self):
        pass

    def __print_footer(self):
        pass

    def output(self):
        self.calculated_measures()
        self.__print_header()
        self.__print_body()
        self.__print_footer()

    def __call__(self):
        try:
            self.output()
        except TypeError:
            pass