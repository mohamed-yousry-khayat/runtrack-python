def calcule(num1, operator, num2):
    if operator == "+":
        resultat = num1 + num2
    if operator == "-":
        resultat = num1 - num2
    if operator == "*":
        resultat = num1 * num2
    if operator == "/":
        resultat = num1 / num2
    if operator == "%":
        resultat = num1 % num2
    return resultat

print(calcule(10, "*", 7))