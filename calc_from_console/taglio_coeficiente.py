
from re import sub
from re import findall


def string_to_list(num_expression):
	s = sub(",", ".", num_expression)
	patern = r"\d+\.\d+|\d+\,\d+|\d+"
	s = findall(patern, s)
	return list(map(lambda x: float(x), s))


def input_coef():
	list_requests = ["misura stoffa", "piega_dentro"]

	def misura_stoffa(answer):
		try:
			return float(input(answer.ljust(22, ' ')))

		except ValueError:
			print("[!] i dati inseriti non sono validi!")
			return misura_stoffa()

	return [misura_stoffa(list_requests[0]),
		string_to_list(input("misura delle tende".ljust(22, ' '))),
		misura_stoffa(list_requests[1])]


def coef(stoffa, list_tend, piega_dentro):
	sum_piega_dentr = (len(list_tend) * 2) * piega_dentro
	cf = (stoffa - sum_piega_dentr) / sum(list_tend)
	print()
	for i in list_tend:
		print(i, "-" * 10, (i * cf) + (2 * piega_dentro))


if __name__ == "__main__":

	lst = input_coef()
	print(coef(lst[0], lst[1], lst[2]))

