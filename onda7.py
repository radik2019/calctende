from colorama import *
"""
module doc
"""


def ond(presunta_misura_bin, passo,  taschini_vuoti):
	"""
	calcoli per la fettuccia da 7 cm

	"""

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
		line = '_' * 40
		binario = coeficiente * passo

		if nod != 0:
			print("\n\n", '*' * 15, " NODI ", '*' * 15)
			while binario < presunta_misura_bin - 1:
				presunta_misura_bin -= nod
				numero_nodi += 1

			misura_effettiva_binario = presunta_misura_bin
		else:
			misura_effettiva_binario = coeficiente * passo
		s = (
			f"{line}\n"
			f"{'binario'.ljust(27, ' ')}{misura_effettiva_binario}\n"
			f"{'ganci'.ljust(27, ' ')}{coeficiente + 1}\n"
			f"{'stoffa'.ljust(27, ' ')}{round((coeficiente * task_sp + 15), 2)}\n"
			f"{'spazio tra ganci'.ljust(27, ' ')}{round(task_sp, 2)}\n"
			f"{'taschini vuoti'.ljust(27, ' ')}{taschini_vuoti }\n"
			f'{"numero nodi".ljust(27, " ")}{numero_nodi}\n'
			f'{line}'
			f"")

		return s

	print(Fore.LIGHTYELLOW_EX, cons())
	if coeficiente * passo < presunta_misura_bin:
		coeficiente += 2
	else:
		coeficiente -= 2
	print(Fore.LIGHTYELLOW_EX, cons())

	print(Fore.LIGHTYELLOW_EX, cons(0.75))

	print(Fore.MAGENTA, f'nella misura della stoffa sono inclusi i 15 cm \n{40 * "*"}')


if __name__ == "__main__":

	ond(241, 8, 7)
	# onda_nod2(231, 8, 6)
	# onda_nod2(214, 8, 6)
	# onda_nod2(187, 8, 6)
	# onda_nod2(322, 8, 6)
