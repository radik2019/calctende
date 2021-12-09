
import pandas as pd


def prezzo_scontato(num, perc):
	try:
		return  num - (perc * num) / 100
	except ZeroDivisionError:
		return num


def input_data():
	global fact

	fact["Prezzo"].append(float(input("Prezzo unitario: ")))
	fact["Nr. pezzi"].append(int(float(input("numero pezzi:    "))))
	fact["Sconto in %"].append(float(input("sconto:          ")))
	tota = fact["Nr. pezzi"][-1] * fact["Prezzo"][-1]

	fact['Prezzo pieno'].append(tota)
	tot_sc = round(prezzo_scontato(fact['Prezzo pieno'][-1], fact["Sconto in %"][-1]), 2)

	fact["Prezzo scontato"].append(tot_sc)


fact = {
    'Prezzo': [],
    'Nr. pezzi': [],
    'Sconto in %': [],
    'Prezzo pieno': [],
    'Prezzo scontato': []
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
	print("totale ========= ",round(sum(fact["Prezzo pieno"]), 2))
	print("totale scontato =", round(sum(fact["Prezzo scontato"]), 2))
	df.to_csv('preventivo.csv')


if __name__ == '__main__':
	start()
