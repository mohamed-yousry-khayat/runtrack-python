def pyramide():
    alph = "abcdefghijklmnopqrstuvwxyz" * 10
    i = 0
    comptage = 0
    tt_comptage = 0
    lettres = ""
    while comptage <= (len(alph) - tt_comptage):
        comptage = 0

        for j in range(tt_comptage, tt_comptage + i + 1):
            lettres = lettres + alph[j]
            comptage = comptage + 1
        print(lettres)

        i = i + 1
        tt_comptage = tt_comptage + i
        lettres = ""


pyramide()
