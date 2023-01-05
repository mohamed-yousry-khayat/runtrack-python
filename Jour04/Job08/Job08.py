def somme_paire():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    total = 0
    for i in L:
        if i%2 == 0:
            total = total + i

    print(total)

somme_paire()