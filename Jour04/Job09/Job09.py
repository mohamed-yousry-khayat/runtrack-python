def max_min():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    verifmax = None
    verifmin = None
    for i in L:
        if verifmax == None:
            verifmax = i
        elif i > verifmax:
            verifmax = i
    print(verifmax)

    for i in L:
        if verifmin == None:
            verifmin = i
        elif i < verifmin:
            verifmin = i
    print(verifmin)

max_min()

#Egalement

def max_mmin2():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    print(max(L))
    print(min(L))


max_mmin2()
