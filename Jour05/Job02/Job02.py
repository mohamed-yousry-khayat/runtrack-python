def rectangle(longueur, largeur):
    for i in range(longueur):
        if i == 0 :
            print("|" + "-" * largeur + "|")
        elif i < (longueur - 1):
            print("|" + " " * largeur + "|")
    print("|" + "-" * largeur + "|")

rectangle(8, 4)
