


class InputError(BaseException):
    pass


class DataInput:
    def __init__(self):
        if self.__class__.__name__ == 'PiegaFissa':
            self.list_ask = ["m. piega:", "m. dentro:", "m. tenda:", "m. stoffa:"]
        if self.__class__.__name__ == 'PiegaTubolare':
            self.list_ask = ['piega:',  'piega dentro:', 'spazio tra pieghe:','misura tenda:', 'stoffa:' ]
        if self.__class__.__name__ == 'StoffaPiegaFissa':
            self.list_ask = ['tenda:', 'piega:', 'piega dentro:']

    def data_input(self):
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
        for ask in self.list_ask:
            data = list_of_measures(ask)
            if not data:
                return None
            list_mis.append(data)
        return list_mis

    def __call__(self):
        return self.data_input()


    def calculatedMeasures(self, func):
        misure = self.data_input()
        if misure:
            return func(misure)
        return


def func(lst):
    for i in lst:
        print(f"----{i}")

