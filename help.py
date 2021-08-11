from colorama import *
bright = Style.BRIGHT
norm = Style.NORMAL
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX



def help():
    help_string = f"""

		{bright}{red}"stp"{norm}{yellow} ---- calcolo della stoffa per la piega fissa'

		{bright}{red}"onda"{norm}{yellow} --- tende a onda
		    onda(binario, passo, misura_onda)

		{bright}{red}"onda7"{norm}{yellow}--- tende a onda con fettuccia da 7 cm
		    ond(presunta_misura_bin, passo,  taschini_vuoti)

		{bright}{red}"piega"{norm}{yellow}--- piega fissa con la fettuccia larga
		    pf([piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa])

		{bright}{red}"nastro"{norm}{yellow}-- nastro barra
		    nastro_barra()

		{bright}{red}"stop"{norm}{yellow}---- chiude il programma 

		{bright}{red}"prop"{norm}{yellow}---- taglio senza spreco scrivere i numeri divisi da spazio, i 
			num non interi vanno scritti con il punto esem.: 2.3 4.67 etc   

		{bright}{red}"ptube"{norm}{yellow}--- piega a tubo
		    pg([misura_tend, misura_stoff, piega, piega_dentro, spazio_tra_pieghe])
		
		{bright}{red}"coef"{norm}{yellow}---- divisione della stoffa per le tende da fare

		{bright}{red}"prev"{norm}{yellow}---- preventivo

		{bright}{red}"steccata"{norm}{yellow}- tenda romana



	"""
    print(help_string)

