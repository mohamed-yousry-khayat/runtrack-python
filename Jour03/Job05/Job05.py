def nombre_premiers():
    nbpremier = 0
    i = 2
    while i < 1000:
        j = 2
        nbnormal = False
        while j <= i//2 and nbnormal == False:
            if i % j == 0:
                nbnormal = True
            else:
                j = j + 1
        if nbnormal == False:
            print(i)
            nbpremier = nbpremier + 1
        i = i + 1


nombre_premiers()
