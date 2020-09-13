

from datetime import datetime
import pickle

def write_pickle(obj):
	with open("journal.pickle", "wb") as df:
		pickle.dump(obj, df)
	return

def read_pickle(file):
	with open(file, "rb") as df:
		obj = pickle.load(df)
	return obj


def add_date():
	lst = []
	s = datetime.now()
	data = f'{s.date()} {s.hour}:{s.minute}'
	name = input("nome:".ljust(19))
	address = input('indirizzo:'.ljust(19))
	
	tipo_tendaggio = input("modello tendaggio".ljust(19))
	if tipo_tendaggio == '':
	    pass
	else:
	    misure = input("misure:".ljust(19))

	lst.append(data)
	lst.append(name)
	lst.append(address)
	lst.append(tipo_tendaggio)
	lst.append(misure)
	lst2 = read_pickle("journal.pickle")
	lst2.append(lst)
	write_pickle(lst2)

def searche():
    sd = read_pickle('journal.pickle')
    std = input('dati da cercare:  ')
    for i in sd:
        for k in i:
            try:
                if std in k:
                    print(f'{"_"*40}\n{i}\n{"_"*40}')                   
            except TypeError:
                pass

   
def show():
    sd = read_pickle('journal.pickle')
    for i in sd:
        print(f'{"_"*40}\n{i}\n{"_"*40}')

if __name__ == '__main__':
    print(
    'stop\nshow\nsearche\nadd_date\n')
    while True:
        dom = input(':  ')
        if dom == 'stop': break
        elif dom == 'show': show()
        elif dom == 'searche': searche()
        elif dom == 'add_date': add_date()
        else: pass