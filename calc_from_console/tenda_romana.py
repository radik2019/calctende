


def t_romana(lst):
    altezza_tenda, fettuccia, basso, bacchette = lst
    bacchette = int(bacchette)
    scesa_bacchetta = 1
    alto = fettuccia - scesa_bacchetta

    parte_da_dividere = altezza_tenda - alto - basso
    # print(parte_da_dividere)


    spazzi = parte_da_dividere / (bacchette  + 1)
    # print(spazzi)
    n = spazzi + alto

    print(n)
    for i in range(bacchette):
        n += spazzi
        print(n)





