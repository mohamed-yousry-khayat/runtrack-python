def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print("triangle valide")
        if a == b == c:
            print("triangle equilateral")
        elif a == b or a == c or b == c:
            print("triangle isocèle")
        elif a^2 == b^2 + c^2 or b^2 == a^2 + c^2 or c^2 == a^2 + c^2:
            print("triangle rectangle")
    else:
        print("triangle non valide")

triangle(3, 5, 4)
