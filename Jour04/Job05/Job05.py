def calcul():
    L = []
    for i in range(1, 6):
        L.append(i)
    print(L[1])
    L.insert(3, L[2]*L[4])
    print(L[4])


calcul()
