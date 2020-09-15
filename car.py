
m = 332
p = 8
t = 6

def onda_nod(misura_bin, passo, taschini_vuoti):
    # taschini_vuoti = int(input('taschini vuoti tra ganci:'.ljust(27, ' ')))
    # misura_bin = float(input('misura binario:'.ljust(27, ' ')))
    # passo = int(input('passo "8" o "6":'.ljust(27, ' ')))
    numero_ganci = misura_bin // passo
    if numero_ganci % 2 == 0:
        numero_ganci += passo
    filo = numero_ganci * passo
    print(numero_ganci)
    print(filo)


onda_nod(m, p, t)









