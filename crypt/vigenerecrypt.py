# vigenerecrypt.py
import utils

vigetab = []


def vigenere(text: str, key: str, mode: str):
    """
    :param text: texte à crypter/decrypter
    :param key: clé de decryptage
    :param mode: mode, decrypt ou crypt
    :return: le text crypté/décrypté
    """

    __create_vigetab()

    if mode == "encrypt":
        return encrypt(text, key)
    else:
        return decrypt(text, key)


def encrypt(text: str, key: str):
    """
    :param text: le texte a crypter
    :param key: string
    :return: string
    """

    text = utils.process_text(text)
    key_adapted = __get_key_adapted(key, len(text), text)
    crypttext = []

    for key, letter in zip(key_adapted, text):
        if letter in vigetab[0]:
            key_index = vigetab[0].index(key)
            letter_index = vigetab[0].index(letter)
            letter = vigetab[key_index][letter_index]
        crypttext.append(letter)

    return "".join(crypttext)


def decrypt(text, key):
    """
    :param text: string
    :param key: string
    :return: string
    """

    key_adapted = __get_key_adapted(key, len(text), text)
    crypttext = []

    for key, letter in zip(key_adapted, text):
        if letter in vigetab[0]:
            key_index = vigetab[0].index(key)
            letter = vigetab[0][vigetab[key_index].index(letter)]
        crypttext.append(letter)
    return "".join(crypttext)


def __get_key_adapted(key: str, length: int, text: str):
    """
    Transforme la clé entrée en une clé adapté au cryptage du texte entré

    :param key: la clé de cryptage/decryptage
    :param length: taille du texte a crypter/decrypter
    :param text: le texte a crypter/decrypter
    :return: string
    """

    key = utils.process_text(key)
    key = key.upper()
    key_length = len(key)
    key_index = 0
    key_adapted = []

    for i in range(0, length):
        if text[i] in vigetab[0]:
            key_adapted.append(key[key_index])
            key_index += 1
            if key_index > key_length - 1:
                key_index = 0
        else:
            key_adapted.append(" ")
    return "".join(key_adapted)


def __create_vigetab():
    """
    :return: talbeau de cyptage en vigenere
    """

    global vigetab
    vigetab = [utils.chrtab()]

    for i in range(1, 26):
        line = utils.decale(vigetab[0], i)
        vigetab.append(line)

    return vigetab
