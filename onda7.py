from colorama import *
"""
module doc
"""


def ond(presunta_misura_bin, passo,  taschini_vuoti):
	"""
	calcoli per la fettuccia da 7 cm
	"""
	# binario singolo o doppio
	


	binario_iniziale = presunta_misura_bin
	def binar():
		tipo_binario = input("[?] binario a 1 telo o 2? [1 / 2]: ")
		if tipo_binario == '2' or tipo_binario == '1':
			return int(tipo_binario)
		else:
			print("[!] inserisci '1' o '2'. indica se l'apertura e' laterale o centrale")
			return binar()

	flag = binar()
	presunta_misura_bin = presunta_misura_bin / flag


	taschini_vuoti -= 1
	task = 52 / 29
	task_sp = task * (taschini_vuoti + 1)
	coeficiente = (presunta_misura_bin // passo)
	if coeficiente % 2 == 0:
		coeficiente += 1
	numero_nodi = 0

	def cons(nod=0.0):
		nonlocal coeficiente
		nonlocal numero_nodi
		nonlocal presunta_misura_bin
		nonlocal flag
		nonlocal binario_iniziale
		line = '_' * 48
		binario = coeficiente * passo
		if nod > 0.0:
			print("\n\n", '*' * 15, " NODI ", '*' * 15)
			if binario < presunta_misura_bin:
				while binario < presunta_misura_bin - 1:
					presunta_misura_bin -= nod
					numero_nodi += 1
			elif binario > presunta_misura_bin:
				while binario > presunta_misura_bin - 1:
					presunta_misura_bin += nod
					numero_nodi += 1

			misura_effettiva_binario = presunta_misura_bin
		else:
			misura_effettiva_binario = coeficiente * passo
		s = (
			f"{line}\n"
			f"{'binario'.ljust(27, ' ')}{misura_effettiva_binario * flag if nod == 0 else binario_iniziale}\n"
			f"{'ganci'.ljust(27, ' ')}{(coeficiente + 1) * flag}\n"
			f"{'stoffa'.ljust(27, ' ')}{round(((coeficiente * task_sp + 15) * flag), 2)}\n"
			f"{'spazio tra ganci'.ljust(27, ' ')}{round(task_sp, 2)}\n"
			f"{'taschini vuoti'.ljust(27, ' ')}{taschini_vuoti }\n"
			f'{"numero nodi".ljust(27, " ")}{numero_nodi * flag}\n'
			f'{line}'
			f"")

		return s

	print(Fore.LIGHTYELLOW_EX, cons())
	if coeficiente * passo < presunta_misura_bin:
		coeficiente += 2
	else:
		coeficiente -= 2
	if flag == 1:
		print("S I N G O L O".center(50, " "))
	elif flag == 2:
		print("D O P P I O".center(50, " "))
	print(Fore.LIGHTYELLOW_EX, cons())

	print(Fore.LIGHTYELLOW_EX, cons(0.75))

	print(Fore.MAGENTA, f'[!] nella misura della stoffa non sono inclusi gli orli o eventuale pieghe dentro \n{40 * "*"}')


if __name__ == "__main__":

	ond(251, 8, 7)

