
def help():
    help_string = """

		"stp" ---- calcolo della stoffa per la piega fissa'

		"onda" --- tende a onda
		    onda(binario, passo, misura_onda)

		"onda7"--- tende a onda con fettuccia da 7 cm
		    ond(presunta_misura_bin, passo,  taschini_vuoti)

		"piega"--- piega fissa con la fettuccia larga
		    pf([piega_aprossimata, piega_dentro, misura_tenda, misura_stoffa])

		"nastro"-- nastro barra
		    nastro_barra()

		"stop"---- chiude il programma 

		"prop"---- taglio senza spreco scrivere i numeri divisi da spazio, i 
			num non interi vanno scritti con il punto esem.: 2.3 4.67 etc   

		"ptube"--- piega a tubo
		    pg([misura_tend, misura_stoff, piega, piega_dentro, spazio_tra_pieghe])
		
		"coef"---- divisione della stoffa per le tende da fare

		"prev"---- preventivo

		"steccata"- tenda romana



	"""
    print(help_string)

