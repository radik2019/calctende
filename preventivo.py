
import pandas as pd


def prezzo_scontato(num, perc):
	try:
		return  num - (perc * num) / 100
	except ZeroDivisionError:
		return num


def input_data():
	global fact

	fact["Prezzo"].append(float(input("Prezzo unitario: ")))
	fact["pezzi"].append(int(float(input("numero pezzi:    "))))
	fact["sconto"].append(float(input("sconto:          ")))
	tota = fact["pezzi"][-1] * fact["Prezzo"][-1]

	fact['pieno'].append(tota)
	tot_sc = prezzo_scontato(fact['pieno'][-1], fact["sconto"][-1])

	fact["scontato"].append(tot_sc)


fact = {
    'Prezzo': [],
    'pezzi': [],
    'sconto': [],
    'pieno': [],
    'scontato': []
}


def start():

	while True:
		a = input("[*] tasto 'invio' per continuare, qualsiasi tasto per interrompere imput\n")
		if a == '':
			input_data()
		else:
			break


	df = pd.DataFrame(fact)
	print("-" * 48)
	print(df)
	print("totale ========= ",sum(fact["pieno"]))
	print("totale scontato =", sum(fact["scontato"]))
	df.to_csv('preventivo.csv')


if __name__ == '__main__':
	start()
