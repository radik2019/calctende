
import pickle



def bi_m():
    with open('onda.pickle', 'rb') as df:
        onda = pickle.load(df)

    
    binario = float(input('misura binario:'.ljust(18, ' ')))
    passo = int(input('passo'.ljust(18, ' ')))
    apertura = input('laterale "l" o centrale "c": ')
    a = onda[apertura][passo]
    temp, i = 0,0
    
    if binario < min(a):
        print('troppo corto')
        return
    spy = 0
    def prynt(a,i):
        print(
            f'{"_" * 40}\n'
            f'{"binario".ljust(14," ")}{i}\n'
            f'{"ganci".ljust(14," ")}{a[i][0]}\n'
            f'{"stoffa".ljust(14," ")}{a[i][1]}\n'
            f'{"_" * 40}\n')
        return ' '
        
    for i in a:
        if apertura == 'c':
            a[i] = list(a[i])
            a[i][0] = f'{a[i][0]} + {a[i][0]}'
        if i == binario:
            prynt(a,i)
            spy += 1
            break
        elif i > binario:
            prynt(a, i)
            print( f'{"oppure".center(40,"*")}')
            prynt(a,temp)
            spy += 1
            break
        else:
            pass
        temp = i
    if spy == 0:
        print('fuorimisura!!!')








