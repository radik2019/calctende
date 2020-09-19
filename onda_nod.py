
"""
module doc
"""




def onda_nod2( presunta_misura_bin, passo,  taschini_vuoti):
	"""
	calcoli per la fettuccia da 7 cm
	:return:
	"""
	taschini_vuoti -= 1

	task = 52 / 29
	task_sp = task * (taschini_vuoti + 1)
	bin = (presunta_misura_bin // passo)
	if bin % 2 == 0:
		bin += 1

	def cons(nod=0.0):
		nonlocal bin
		# numero_nodi = 0

		line = '_' * 40

		binario = bin * passo
		numero_nodi = 0
		if nod != 0:
			print("\n\n", '*' * 15," NODI ",'*' * 15 )
			print(bin)
			while binario > (presunta_misura_bin - 1):
				binario -= nod
				numero_nodi += 1
				print(numero_nodi)
		else:
			pass
		s = (
			f"{line}\n"
			f"{'binario'.ljust(27, ' ')}{bin * passo}\n"
			f"{'ganci'.ljust(27, ' ')}{bin + 1}\n"
			f"{'stoffa'.ljust(27, ' ')}{round((bin * task_sp + 15), 2)}\n"
			f"{'coeficiente'.ljust(27, ' ')}{round((task_sp), 2)}"
			f'\n{"numero nodi".ljust(27, " ")}{numero_nodi}\n'
			f'{line}'
			f"")
		print(s)


	cons()
	if bin * passo < presunta_misura_bin:
		bin += 2
	else:
		bin -= 2
	cons()

	cons(0.75)

	print(f'nella misura della stoffa sono inclusi i 15 cm \n{40 * "*"}\n'
		  f"{'taschini vuoti'.ljust(27, ' ')}{taschini_vuoti}")



if __name__ == "__main__":

	onda_nod2(241,8,6)