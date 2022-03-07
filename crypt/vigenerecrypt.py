# vigenerecrypt.py
import utils

vigetab = []


def vigenere(text: str, key: str, mode: str):
    """
    Choisit la bonne mode de cryptage en fonction du mode, crypte en Vigenère

    :param text: Le texte à crypter/décrypter
    :param key: Clé de cryptage/décryptage
    :param mode: Mode, "encrypt" ou "decrypt"
    :return: Le text crypter/décrypter
    """

    global vigetab  # On utilise la variable globale pour qu'elle soit accessible depuis toutes les fonctions
    vigetab = __create_vigetab()

    text = utils.process_text(text)

    if mode == "encrypt":
        return __encrypt(text, key)
    else:
        return __decrypt(text, key)


def __encrypt(text: str, key: str):
    """
    Crypte le texte entré en Vigenère

    :param text: Texte à crypter
    :return: Texte crypté
    """

    key_adapted = __get_key_adapted(key, len(text), text)
    crypttext = []

    for key, letter in zip(key_adapted, text):  # On parcourt à la fois key_adapted et text grâce à zip
        if letter in vigetab[0]:  # On vérifie bien que la lettre est bien cryptable, sinon on l'ajoute sans cryptage

            # On prend les deux index sur la première ligne ça revient au même que de prendre dans la colonne
            key_index = vigetab[0].index(key)
            letter_index = vigetab[0].index(letter)
            letter = vigetab[key_index][letter_index]

        crypttext.append(letter)

    return "".join(crypttext)


def __decrypt(text, key):
    """
    Décrypte le texte entré en Vigenère

    :param text: Texte à décrypter
    :return: Texte décrypté
    """

    key_adapted = __get_key_adapted(key, len(text), text)
    crypttext = []

    for key, letter in zip(key_adapted, text):  # On parcourt à la fois key_adapted et text grâce à zip
        if letter in vigetab[0]:  # On vérifie bien que la lettre est bien cryptable, sinon on l'ajoute sans cryptage
            key_index = vigetab[0].index(key)
            letter = vigetab[0][vigetab[key_index].index(letter)]

        crypttext.append(letter)

    return "".join(crypttext)


def __get_key_adapted(key: str, length: int, text: str):
    """
    Transforme la clé entrée en une clé adaptée au cryptage du texte entré

    :param key: la clé de cryptage/decryptage
    :param length: taille du texte à crypter/decrypter
    :param text: le texte à crypter/decrypter
    :return: la clé adaptée au texte
    """

    key = utils.process_text(key)
    key = key.upper()
    key_length = len(key)
    key_index = 0
    key_adapted = []

    for i in range(0, length):
        if text[i] in vigetab[0]:  # On vérifie bien que la lettre est bien pour éviter les problèmes avec les espaces

            key_adapted.append(key[key_index])
            key_index += 1
            if key_index > key_length - 1:
                key_index = 0

        else:
            key_adapted.append(" ")

    return "".join(key_adapted)


def __create_vigetab():
    """
    Crée un tableau de Vigenère

    :return: talbeau de cyptage en vigenere
    """

    tab = [utils.chrtab()]

    for i in range(1, 26):
        line = utils.decale(tab[0], i)  # Utilisation de ma librairie pour decalé de 1 de plus à chaque fois
        tab.append(line)

    return tab
