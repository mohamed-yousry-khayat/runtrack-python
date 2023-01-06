def crypt():
    cle = 12
    message_a_crypter = input()
    longueur = len(message_a_crypter)
    message_crypte = ""

    for i in range(longueur):
        if message_a_crypter[i] == ' ':
            message_crypte += ' '
        else:
            asc = ord(message_a_crypter[i]) + cle
            message_crypte += chr(asc + 26 * ((asc < 65) - (asc > 90)))

    print(message_crypte)


crypt()
