

import pandas as pd




def prezzo_scontato(num, perc):
	try:
		return  num - (perc * num) / 100
	except ZeroDivisionError:
		return num


def input_data():
	global fact
	lst = [
		"Prezzo unitario: ",
		"numero pezzi:    ",
		"sconto:          ",
	]
	lst2 = ['Prezzo', 'pezzi', 'sconto']
	for i in range(len(lst)):
		fact[lst2[i]].append(float(input(lst[i])))

	tota = fact["pezzi"][-1] * fact["Prezzo"][-1]

	fact['pieno'].append(tota)
	tot_sc = prezzo_scontato(fact['pieno'][-1], fact["sconto"][-1])

	
	fact["scontato"].append(tot_sc)


def input_data2():
	pass



fact = {
    'Prezzo': [],
    'pezzi': [],
    'sconto': [],
    'pieno': [],
    'scontato': []
}

while True:
	a = input("[*] tasto 'invio' per continuare, qualsiasi tasto per interrompere imput\n")
	if a == '':
		input_data()
	else:
		break



df = pd.DataFrame(fact)

print(df)
print("totale ========= ",sum(fact["pieno"]))
print("totale scontato =", sum(fact["scontato"]))
df.to_csv('preventivo.csv')







