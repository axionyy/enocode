from pyperclip import *


def copyresault(a):
    copy(a)


def pastecopyed():
    return paste()


def cezar_enocode(message, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
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
    resault = ""
    text = message.upper()

    for i in text:
        mesto = ruUpperLetters.find(i)  # Алгоритм для дешифрования сообщения на русском
        new_mesto = (mesto - key) % 33
        if i in ruUpperLetters:
            resault += ruUpperLetters[new_mesto]
        else:
            resault += i
    return resault.lower()


def vizhener_enocode(text, key):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    enocode_text = ''
    key_length = len(key)
    key_index = 0

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % key_length]
            key_char_index = alphabet.index(key_char)
            encrypted_char_index = (char_index + key_char_index) % len(alphabet)
            encrypted_char = alphabet[encrypted_char_index]
            enocode_text += encrypted_char
            key_index += 1
        else:
            enocode_text += char

    return enocode_text


def vizhener_decode(text, key):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    decode_text = ''
    key_length = len(key)
    key_index = 0

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % key_length]
            key_char_index = alphabet.index(key_char)
            decrypted_char_index = (char_index - key_char_index) % len(alphabet)
            decrypted_char = alphabet[decrypted_char_index]
            decode_text += decrypted_char
            key_index += 1
        else:
            decode_text += char

    return decode_text


def hex_enocode(text):
    encode_text3 = text.encode('utf-8').hex()
    return encode_text3


def hex_decode(encode_text3):
    decode_text3 = bytes.fromhex(encode_text3).decode('utf-8')
    return decode_text3


def atbash_cipher(text):
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = ""

        for char in text:
            if char.isalpha():
                if char.isupper():
                    index = alphabet.index(char.lower())
                    replaced_char = alphabet[::-1][index].upper()
                else:
                    index = alphabet.index(char)
                    replaced_char = alphabet[::-1][index]
                result += replaced_char
            else:
                result += char

        return result


def atbash_decipher(ciphertext):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                index = alphabet[::-1].index(char.lower())
                replaced_char = alphabet[index].upper()
            else:
                index = alphabet[::-1].index(char)
                replaced_char = alphabet[index]
            result += replaced_char
        else:
            result += char

    return result