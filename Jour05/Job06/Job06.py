def math():
    L = [55, 54, 40, 39, 42, 43, 100, 99]
    L2 = []
    for i in L:
        if i <= 40:
            L2.append(i)
        if i > 40:
            if i%5 > 2:
                while i%5 != 0:
                    i = i + 1
                L2.append(i)
            else:
                L2.append(i)
    print(L2)

math()
