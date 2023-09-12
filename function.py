def cezar_enocode(message, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    engUpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resault = ""

    text = message.upper()


    for i in text:
        mesto = ruUpperLetters.find(i)  # Алгоритм для шифрования сообщения на русском
        new_mesto = (mesto + key) % 33
        if i in ruUpperLetters:
            resault += ruUpperLetters[new_mesto]
        else:
            resault += i
    return resault.lower()


def cezar_decode(message, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    engUpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resault = ""

    text = message.upper()


    for i in text:
        mesto = ruUpperLetters.find(i)  # Алгоритм для шифрования сообщения на русском
        new_mesto = (mesto - key) % 33
        if i in ruUpperLetters:
            resault += ruUpperLetters[new_mesto]
        else:
            resault += i
    return resault.lower()