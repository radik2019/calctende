from re import sub
from re import findall

def input_coef():
	pass


def coef(stoffa, list_tend, piega_dentro):
	sum_piega_dentr = (len(list_tend) * 2) * piega_dentro
	cf = (stoffa - sum_piega_dentr) / sum(list_tend)

	lst = []
	for i in list_tend:
		print((i * cf) + (2 * piega_dentro))
		lst.append((i * cf) + (2 * piega_dentro))

	print(sum(lst))

	
def string_to_list(num_expression):
	s = sub(",", ".", num_expression)
	patern = r"\d+\.\d+|\d+\,\d+|\d+"
	s = findall(patern, s)
	return list(map(lambda x: float(x), s))


if __name__ == "__main__":

	print(coef(591, [160, 130], 12))

	print(string_to_list("23,23 434k2h234 234k2323.422j23hklj3"))


