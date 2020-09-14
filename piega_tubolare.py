


def pg_input():
    m_tend = float(input('misura tenda:'.ljust(22, ' ')))
    m_stoff = float(input('stoffa'.ljust(22, ' ')))
    piega = float(input('piega:'.ljust(22, ' ')))
    piega_den = float(input('piega dentro:'.ljust(22, ' ')))
    space = float(input('spazio tra pieghe:'.ljust(22, ' ')))
    return [m_tend, m_stoff, piega, piega_den, space]


def pg_input2():
    def mis_tend():
        try:
            m_tend = float(input('misura tenda:'.ljust(22, ' ')))
        except ValueError:
            print("[!] i dati inseriti non sono validi!")


def pg(lst):
    m_tend, m_stoff, piega, piega_den, space = lst

    coef = (m_tend + space) // (space + piega)
    piega = ((m_tend + space) / coef) - space
    interval = ((m_stoff - (piega_den * 2) - m_tend) / (coef - 1)) / 2
    print(
        f"{'_' * 40}\n"
        f"{'piega'.ljust(15, ' ')}{round(piega, 1)}\n"
        f"{'spazio'.ljust(15, ' ')}{round(space, 1)}\n"
        f"{'intervallo'.ljust(15, ' ')}{round(interval, 1)}\n"
        f"{'_' * 40}\n"
    )

    i = 0
    while i < m_stoff:
        i += piega
        print('piega'.ljust(14, " "), round(i, 1))
        i += interval
        print("interval".ljust(14, " "), round(i, 1))
        i += space
        print("spazio".ljust(14, " "), round(i, 1))
        i += interval
        print("intervallo ".ljust(14, " "), round(i, 1), end="\n\n")
    print(f"sarebbe perfetta con questa metratura di stoffa "
          f""
          f"{round((piega * (coef * 2) + ((coef - 1) * space)) + (piega_den * 2), 1)}")





