

def ond( presunta_misura_bin, passo,  taschini_vuoti):
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

    def cons():
        print(
            f"{'_' * 40}\n"
            f"{'binario'.ljust(27, ' ')}{bin * passo}\n"
            f"{'ganci'.ljust(27, ' ')}{bin + 1}\n"
            f"{'stoffa'.ljust(27, ' ')}{round((bin * task_sp + 15), 2)}\n"
            f"{'coeficiente'.ljust(27, ' ')}{round((task_sp), 2)}\n{'_' * 40}"
            f""
        )

    cons()
    if bin * passo < presunta_misura_bin:
        bin += 2
    else:
        bin -= 2
    cons()
    print(f'nella misura della stoffa sono inclusi i 15 cm \n{40 * "*"}\n'
          f"{'taschini vuoti'.ljust(27, ' ')}{taschini_vuoti}"
          )
