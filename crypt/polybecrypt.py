# polybecrypt.py
import utils

poltab = []
chrtab = utils.chrtab()
numtab = [str(x) for x in range(1,10)]


def polybe(text: str, key: str, mode: str):
    key = key.upper()
    global poltab
    poltab = __create_poltab(key)

    text = utils.process_text(text)
    text = text.upper()

    if mode == "encrypt":
        return encrypt(text)
    else:
        return decrypt(text)


def encrypt(text: str):

    text = text.upper()
    crypttext = []

    for letter in text:
        if letter in chrtab:
            x, y = __index_letter(letter)
            num = str(x + 1) + str(y + 1)
            crypttext.append(num)

        else:
            crypttext.append(letter)

    return "".join(crypttext)


def decrypt(text: str):
    """
    Décrypte de le etxte entré

    :param text: Texte à décrypter
    :return: Le texte décrypté
    """

    crypttext = []
    pair = ""

    for num in text:
        if num in numtab:
            pair += num
            if len(pair) == 2:
                decrypt_letter = poltab[int(pair[0])-1][int(pair[1])-1]
                crypttext.append(decrypt_letter)
                pair = ""
        else:
            crypttext.append(num)

    return "".join(crypttext)


def __index_letter(letter: str):
    """
    Retourne les coordonnée dans le tableau de polybe de la lettre entrée

    :param letter: Lettre à retrouver
    :return: Les coordonnées de la lettre cherchée
    """

    for i, line in enumerate(poltab):
        if letter in line:
            return i, line.index(letter)


def __create_poltab(key: str):
    """
    Crée le carré de Polybe qui sera utilisé pour crypter et décrypter le tableau doit être entré sous forme
    linéaire, ex : AZERTYUIOPQSDFGHJKLMWXCVB

    :param key: Clé qui permettra de créer le tableau
    :return: Un carré de polybe
    """

    for i in range(5):
        poltab.append([])
        for j in range(5):
            letter = key[j + (i * 5)]
            poltab[i].append(letter)
    return poltab

