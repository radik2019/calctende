
from data_input import *



class StoffaPiegaFissa(DataInput):
    def __init__(self, *args):
        super().__init__(*args)
        self.numero_di_pieghe: int = self.tenda // self.piega
        self.piega = self.tenda / self.numero_di_pieghe
        self.numero_di_pieghe: int = self.tenda // self.piega
        self.piega = self.tenda / self.numero_di_pieghe
        if max(self.piega_dentro, self.piega) >self.tenda :
            raise InputError("[ ! ] Inserisci dati sensati blea")

    def calculated_measures(self):
        stoffa = (((self.piega * self.numero_di_pieghe) + ((self.piega * 2) 
        * (self.numero_di_pieghe - 1))) + (self.piega_dentro * 2))
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