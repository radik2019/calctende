
list_ask_tub = [
    'misura tenda:',
    'stoffa:',
    'piega:',
    'piega dentro:',
    'spazio tra pieghe:'
]
"""
piega tubolare
"""


class PiegaTubolare:
    def __init__(self, m_tend=None, m_stoff=None, piega=None, piega_den=None, space=None):
        if all((m_tend, m_stoff, piega, piega_den, space)):
            self.m_tend = m_tend
            self.m_stoff = m_stoff
            self.piega = piega
            self.piega_den = piega_den
            self.space = space
        else:
            self.readyToInput = self.data_input()
            self.m_tend, self.m_stoff,self.piega, self.piega_den, self.space = self.readyToInput




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
