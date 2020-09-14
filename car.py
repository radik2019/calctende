


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
            return m_tend
        except ValueError:
            print("[!] i dati inseriti non sono validi!")
            return mis_tend()
    m_tend = mis_tend()
    return m_tend
print(pg_input2())