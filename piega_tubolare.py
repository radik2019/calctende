from data_input import *


class PiegaTubolare(DataInput):
    """calcoli per la tenda a pieghe tublolari"""

    def __init__(self, *args):
        super().__init__()
        if all(args) and len(args) == 5:
            if max(args[0], args[1], args[2]) < args[3] < args[4]:
                self.piega = args[0]
                self.piega_den = args[1]
                self.space = args[2]
                self.m_tend = args[3]
                self.m_stoff = args[4]
                self.lst = []
                self.coeficente: int = 0
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")
        else:
            self.readyToInput = self.data_input()
            if (max(self.readyToInput[0], self.readyToInput[1], self.readyToInput[2]) \
                    < self.readyToInput[3] < self.readyToInput[4]):
                self.piega, self.piega_den, self.space, self.m_tend, self.m_stoff = self.readyToInput
                self.lst = []
                self.coeficente: int = 0
            else:
                raise InputError("[ ! ] Inserisci dati sensati blea")

    def __print_header(self):
        print(
            f"{'_' * 40}\n"
            f"{'piega'.ljust(15, ' ')}{round(self.piega, 1)}\n"
            f"{'spazio'.ljust(15, ' ')}{round(self.space, 1)}\n"
            f"{'intervallo'.ljust(15, ' ')}{round(self.interval, 1)}\n"
            f"{'_' * 40}\n")

    def __print_footer(self):
        print(f"sarebbe perfetta con questa metratura di stoffa "
              f""
              f"{round((self.piega * (self.coeficente * 2) + ((self.coeficente - 1) * self.space)) + (self.piega_den * 2), 1)}")

    def calculated_measures(self) -> None:
        self.coeficente = (self.m_tend + self.space) // (self.space + self.piega)
        self.piega = ((self.m_tend + self.space) / self.coeficente) - self.space
        self.interval = ((self.m_stoff - (self.piega_den * 2) - self.m_tend) / (self.coeficente - 1)) / 2

        i = 0
        while i < self.m_stoff:
            i += self.piega
            self.lst.append(round(i, 1))
            i += self.interval
            self.lst.append(round(i, 1))
            i += self.space
            self.lst.append(round(i, 1))
            i += self.interval
            self.lst.append(round(i, 1))

    def __print_body(self):
        for i in range(0, len(self.lst), 4):
            print('piega'.ljust(14, " "), round(self.lst[i], 1))
            print("interval".ljust(14, " "), round(self.lst[i + 1], 1))
            print("spazio".ljust(14, " "), round(self.lst[i + 2], 1))
            print("intervallo ".ljust(14, " "), round(self.lst[i + 3], 1), end="\n\n")

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

if __name__ == "__main__":
    PiegaTubolare()()






