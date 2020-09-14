


def pg_input3():
    def list_of_measures(s):
        try:
            question = float(input(s.ljust(22, ' ')))
            return question
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            return list_of_measures(s)

    list_ask = [
        'misura tenda:',
        'stoffa:',
        'piega:',
        'piega dentro:',
        'spazio tra pieghe:'
    ]
    list_mis = []

    for ask in list_ask:
        list_mis.append(list_of_measures(ask))


    return list_mis

print(pg_input3())












