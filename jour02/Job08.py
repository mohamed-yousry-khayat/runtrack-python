def fruit_legume(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        print("poire, fraise et cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour et endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine et navet")

fruit_legume("fruit", "ete")