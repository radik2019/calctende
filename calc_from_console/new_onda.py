
from colorama import *
from data_input import *
from globals import PRINT_WIDTH


class Onda(DataInput):
	"""
	passo: 8 or 6
	taschini_vuoti................: 67.0
	binary_type...................: 67.0
	presunta_misura_bin...........: 67.0
	fettuccia.....................: 76.0
	"""
	def __init__(self, *args):
		super().__init__(*args)
		if not ((self.passo == 8 or self.passo == 6) and (1 < self.taschini_vuoti < 15) and
		(self.fettuccia == 7 or self.fettuccia == 9) and (0 < self.binary_type < 2)):
			raise InputError("Hai inserito un dato errato")

	@staticmethod
	def __print_header(self):
		print(Fore.RED + "[!]" + Fore.YELLOW + " '7 GANCI VUOTI = 14.34 cm con la fettuccia da 7 cm" + Fore.LIGHTGREEN_EX)
		print(Fore.RED + "[!]" + Fore.YELLOW + " '3 GANCI VUOTI = 14.46 cm con la fettuccia da 9 cm" + Fore.LIGHTGREEN_EX)

	def __repr__(self):

		s = f'\n\n.... {self.__class__.__name__} ...\n'
		for i in self.__dict__:
			s += f'{i}'.ljust(PRINT_WIDTH, '.') + ': ' + f"{self.__dict__[i]}" + '\n'
		return s


if __name__ == "__main__":

	df = Onda()
	print(df)

	def check_app(obj):
		try:
			obj()()
		except TypeError:
			pass
	# check_app(Onda)




