

from globals import PRINT_WIDTH, INPUT_VARIABLE

class InputError(BaseException):
    pass


class DataInput:


    def __new__(cls, *args):

        if cls.__name__ in INPUT_VARIABLE:
            if len(args) == len(INPUT_VARIABLE[cls.__name__][0]):
                return object.__new__(cls)
            elif len(args) == 0:
                return object.__new__(cls)
            else:
                raise InputError("Numero di dati inseriti errato")
        else:
            raise InputError(f"La classe {cls.__name__} non e nel database")

    def __init__(self, *args):
        self.list_ask = INPUT_VARIABLE[self.__class__.__name__][1]
        if len(args) > 0:
            if len(args) == len(INPUT_VARIABLE[self.__class__.__name__][0]):
                for i in range(len(args)):

                    self.__dict__[INPUT_VARIABLE[self.__class__.__name__][0][i]] = args[i]
        elif len(args) == 0:
            lst = self.data_input()

            for i in range(len(lst)):
                self.__dict__[INPUT_VARIABLE[self.__class__.__name__][0][i]]  = lst[i]

    

    def data_input(self):
        def list_of_measures(s):
            try:
                question = input(s.ljust(PRINT_WIDTH, '.') + ': ')
                if question.lower() == "stop":
                    return None
                question = float(question)
                return question
            except ValueError:
                print("[!] i dati inseriti non sono validi!")
                return list_of_measures(s)
        list_mis = []
        for ask in self.list_ask:
            data = list_of_measures(ask)
            if not data:
                return None
            list_mis.append(data)
        return list_mis

    def calculatedMeasures(self, func):
        misure = self.data_input()
        if misure:
            return func(misure)
        return



