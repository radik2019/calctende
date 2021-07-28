
from itertools import combinations

from re import findall
from re import sub

# 23,4 34,5 45.56 23.34 12,21 23 19
# 128 231


def string_to_list(nm):
    
    if '(' in nm:
        start = nm.index('(')
        stop = nm.index(')')
        subs = nm[start+1:stop]
        nm = nm[:start] + nm[stop+1:]
        s = sub(",", ".", subs)
        patern = r"\d+\.\d+|\d+\,\d+|\d+"
        s = findall(patern, s)
        #print(nm)
        subs = (s[0] + ' ') * int(s[1])
        return string_to_list(nm + ' '+ subs)
         
        
    s = sub(",", ".", nm)
    patern = r"\d+\.\d+|\d+\,\d+|\d+"
    s = findall(patern, s)
    return list(map(lambda x: float(x), s))


def prop():
    
    def prop_n(lst2, n):
        a = 0
        ls = []
        for item in range(len(lst2) + 1):
            ab = combinations(lst2, item)
            for k in ab:
                if a < sum(k) <= n:
                    a = sum(k)
                    ls = k
                else:
                    pass
        return ls

    def choice_list(sottopezzi, pezzi, index_n):

        for piece in pezzi:
            lst.append(prop_n(sottopezzi, piece))
            sum_list.append(piece - sum(prop_n(sottopezzi, piece)))
        # print(sum_list)
        ind = sum_list.index(min(sum_list))

        df[f'{index_n}) {pezzi.pop(ind)}'] = lst[ind]

        for k in lst[ind]:
            sottopezzi.remove(k)
        return

    index_n = 1
    sottopezzi = string_to_list(input('misure da ottenere:  '))
    pezzi = string_to_list(input('misure da dividere:  '))
    df = {}
    while len(sottopezzi) > 0 and len(pezzi) > 0:
        lst = []
        sum_list = []
        choice_list(sottopezzi, pezzi, index_n)
        index_n += 1
    resti = []
    for i in df:
        print('_' * 50)
        # print(f'{i} -- {df[i]}\nresto -- {i - sum(df[i])}')
        print(f'{i} -- {sum(df[i])} = {df[i]}')
        if (float(i[3:]) - sum(df[i])) != 0:
            resti.append(round(float(i[3:]) - sum(df[i]), 2))

    print('_' * 50)
    # print(f'manca materiale per: {sottopezzi}')
    print(f'avanzano pezzi:        {resti}')
    print(f'interi avanzati        {pezzi}')
    return ' '


if __name__ == "__main__":
    prop()
    




