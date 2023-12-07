from colorama import *
import os
import sys, json

LARGE = 40
LINE = Fore.RED + ('_' * LARGE) + Fore.LIGHTYELLOW_EX +'\n' 
"""
module doc
"""

dct = {
    "onda": [[52, 29], [126.5, 35]],
    "prezzo_onda":20,
    "prezzo_piegafissa":20,
    "arriccia_tenda": 14,
    "orli": 5,
}


def json_write(file, data):
    with open(file, "w") as write_file:
        json.dump(data, write_file)


def json_read(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


