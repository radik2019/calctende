

import time
import random


class Input:
    def __init__(self):
        self.f = 'sono la funzione f'
        self.s = 'sono la funzione s'
    def get_data(self):
        if self.__class__.__name__ == "First":
            return self.f
        elif self.__class__.__name__ == "Second":
            return self.s

class First(Input):
    pass

class Second(Input):
    pass

# nm = First()
# nm2 = Second()

# print(nm.get_data())
# print(nm2.get_data())

def data_input(list_ask):
    def list_of_measures(s):
        try:
            question = input(s.ljust(22, ' '))
            if question.lower() == "stop":
                return None
            question = float(question)
            return question
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            return list_of_measures(s)
    list_mis = []
    for ask in list_ask:
        data = list_of_measures(ask)
        if not data:
            return None
        list_mis.append(data)
    return list_mis


