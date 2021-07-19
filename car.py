
import os, sys, re


def read_proportion(flag: int = 0 )->list:
    """scelta del tipo di fettuccia"""
    lst = os.listdir()
    if sys.platform == "linux":
        CLEAR_SCREEN = "clear"
    elif sys.platform == "win32":
        CLEAR_SCREEN = "cls"
        init(convert=True)
    if "fettuccia_onda.txt" in lst:
        with open("fettuccia_onda.txt", "r") as df:
            data = df.read()
        numb = data.split('\n')

        numb = [re.findall(r"\d+\.\d+|\d+\,\d+|\d+", i) for i in numb]
        numb = [[float(k) for k in i] for i in numb]
        return numb[flag]
    else:
        with open("fettuccia_onda.txt", "w") as dg:
            dg.write("52  29 \n 126.5  35")
        read_proportion()



print(read_proportion())

