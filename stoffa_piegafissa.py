list_ask_stoffa = ['tenda:', 'piega:', 'piega dentro:']


def stoffa_per_piega_fissa(list_ask):
    """
    si calcola la stoffa per la piega fissa.
    nel risultato si include anche la piega dentro
    :return: quanta stoffa devi avere
    """

    tenda, piega, piega_dentro = list_ask
    sa = tenda // piega
    coef = tenda / sa
    print('_' * 50)
    print(f'stoffa:\t{((coef * sa) + ((coef * 2) * (sa - 1))) + (piega_dentro * 2)}')
    print(f'piega:\t{coef}')
    print('_' * 50)
