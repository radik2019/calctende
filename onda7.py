# from colorama import *
# """
# module doc
# """


# def ond(presunta_misura_bin, passo,  taschini_vuoti, flag):
# 	WIDTH = 45
# 	"""
# 	calcoli per la fettuccia da 7 cm
# 	"""
# 	binario_iniziale = presunta_misura_bin
	
# 	# binario singolo o doppio

# 	# def binar():
# 	# 	tipo_binario = input("[?] binario a 1 telo o 2? [1 / 2]: ")
# 	# 	if tipo_binario == '2' or tipo_binario == '1':
# 	# 		return int(tipo_binario)
# 	# 	else:
# 	# 		print("[!] inserisci '1' o '2'. indica se l'apertura e' laterale o centrale")
# 	# 		return binar()

# 	# flag = binar()
# 	presunta_misura_bin = presunta_misura_bin / flag


# 	taschini_vuoti -= 1
# 	task = 52 / 29
# 	task_sp = task * (taschini_vuoti + 1)
# 	coeficiente = (presunta_misura_bin // passo)
# 	if coeficiente % 2 == 0:
# 		coeficiente += 1
# 	numero_nodi = 0

# 	def cons(nod=0.0):
# 		nonlocal coeficiente
# 		nonlocal numero_nodi
# 		nonlocal presunta_misura_bin
# 		nonlocal flag
# 		nonlocal binario_iniziale
# 		line = '_' * WIDTH
# 		binario = coeficiente * passo
# 		if nod > 0.0:

# 			print("  N O D I  ".center(WIDTH, "*"))
# 			if binario < presunta_misura_bin:
# 				while binario < presunta_misura_bin - 1:
# 					presunta_misura_bin -= nod
# 					numero_nodi += 1
# 			elif binario > presunta_misura_bin:
# 				while binario > presunta_misura_bin - 1:
# 					presunta_misura_bin += nod
# 					numero_nodi += 1

# 			misura_effettiva_binario = presunta_misura_bin
# 		else:
# 			misura_effettiva_binario = coeficiente * passo
# 		s = (
# 			f"{line}\n"
# 			f"{'binario'.ljust(27, ' ')}{misura_effettiva_binario * flag if nod == 0 else binario_iniziale}\n"
# 			f"{'ganci'.ljust(27, ' ')}{(coeficiente + 1) * flag}\n"
# 			f"{'stoffa'.ljust(27, ' ')}{round(((coeficiente * task_sp + 15) * flag), 2)}\n"
# 			f"{'spazio tra ganci'.ljust(27, ' ')}{round(task_sp, 2)}\n"
# 			f"{'taschini vuoti'.ljust(27, ' ')}{taschini_vuoti }\n"
# 			f'{"numero nodi".ljust(27, " ")}{numero_nodi * flag}\n'
# 			f'{line}'
# 			f"")

# 		return s

# 	print(Fore.LIGHTYELLOW_EX + cons())
# 	if coeficiente * passo < presunta_misura_bin:
# 		coeficiente += 2
# 	else:
# 		coeficiente -= 2
# 	if flag == 1:
# 		print("S I N G O L O".center(WIDTH, " "))
# 	elif flag == 2:
# 		print("D O P P I O".center(WIDTH, " "))
# 	print(Fore.LIGHTYELLOW_EX + cons())

# 	print(Fore.LIGHTYELLOW_EX + cons(0.75))

# 	print(Fore.MAGENTA + f'[!] nella misura della stoffa non sono inclusi gli orli o eventuale pieghe dentro \n{WIDTH * "*"}')


# if __name__ == "__main__":

# 	ond(251, 8, 7, 1)




from colorama import *
LINE = '_' * 50 + '\n'
"""
module doc
"""


def binar():
    tipo_binario = input("[?] binario a 1 telo o 2? [1 / 2]: ")
    if tipo_binario == '2' or tipo_binario == '1':
        return int(tipo_binario)
    else:
        print("[!] inserisci '1' o '2'. indica se l'apertura e' laterale o centrale")
        return binar()

def calcolo_nodi(misura_bin, passo, larghezza_massima_binario, presunta_misura_bin):
    misura_bin += (passo * 2)
    da_dividere_per_nodi = larghezza_massima_binario - presunta_misura_bin
    numero_nodi = int(da_dividere_per_nodi / 0.75)
    return numero_nodi

def calcolo_ond(presunta_misura_bin,
    passo,
    taschini_vuoti, #numero di taschini vuoti tra i ganci
    binary_type = 1,
    nodi="high" #puo essere "high", "low", "node"
    ):
    
    # distanza tra taschini
    dist_task = 52 / 29
    numero_ganci = 0
    
    final_result = [0, 0, 0, 0] # [binario, stoffa, numero_ganci, numero_nodi_da_fare]
    if binary_type == 1:
        pass
    else:
        presunta_misura_bin /= 2

    # calcolo del numero degli spazi tra gamci
    spazi_tra_ganci = presunta_misura_bin // passo
    if spazi_tra_ganci % 2 == 0:
        spazi_tra_ganci -= 1
    misura_bin = spazi_tra_ganci * passo
    # print("misura binario - ", misura_bin)

    larghezza_massima_binario = misura_bin + (passo * 2)

    if nodi == "high":
        misura_bin += (passo * 2)
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)

    if nodi == "low":
        final_result[0] = misura_bin if binary_type == 1 else misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2
        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)

    if nodi == "node":
        if misura_bin < presunta_misura_bin:
            misura_bin += (passo * 2)
        final_result[0] = presunta_misura_bin if binary_type == 1 else presunta_misura_bin * 2
        final_result[1] = round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2)\
        if binary_type == 1 else round(((misura_bin / passo) * dist_task * (taschini_vuoti + 1)) + 15, 2) * 2

        final_result[2] = round(dist_task * (taschini_vuoti + 1), 2)
        final_result[3] = calcolo_nodi(misura_bin, passo, larghezza_massima_binario, presunta_misura_bin)

    return final_result


def print_ond(mis_ef, stoff, spaz_ganc, nodi):
    s = (
        Fore.LIGHTYELLOW_EX + f"{LINE}\n"
        f"{'binario'.ljust(27, ' ')}{mis_ef}\n"
        f"{'stoffa'.ljust(27, ' ')}{stoff}\n"
        f"{'spazio tra ganci'.ljust(27, ' ')}{spaz_ganc}\n"
        )
    s= s + f'{"numero nodi".ljust(27, " ")}{nodi}\n' if nodi > 0 else s
    s = s +LINE
    print(s)
    return ''


def ond(presunta_misura_bin, passo,  taschini_vuoti, binary_type):
    """
    calcoli per la fettuccia da 7 cm
    """
    print(LINE)
    misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "low")

    misura_effettiva_binario2, stoffa2, spazio_tra_ganci2, nodi2 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "high")

    misura_effettiva_binario3, stoffa3, spazio_tra_ganci3, nodi3 = calcolo_ond(presunta_misura_bin,\
        passo, taschini_vuoti, binary_type, "node")
    print("S I N G O L O".center(50, " ") if binary_type == 1 else "D O P P I O".center(50, " "))
    if misura_effettiva_binario1 == presunta_misura_bin:
        print_ond(misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1)
    else:	
        print_ond(misura_effettiva_binario1, stoffa1, spazio_tra_ganci1, nodi1)
        print_ond(misura_effettiva_binario2, stoffa2, spazio_tra_ganci2, nodi2)
        print("  N O D I  ".center(50, "*"))
        print_ond(misura_effettiva_binario3, stoffa3, spazio_tra_ganci3, nodi3)
    return

if __name__ == "__main__":
    ond(388, 8, 7, 1)
    print()

