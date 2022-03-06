# polybecrypt.py
import utils


def __create_poltab(key: str):
    """
    Crée le carré de Polybe qui sera utilisé pour crypter et décrypter le tableau doit être entré sous forme
    linéaire, ex : AZERTYUIOPQSDFGHJKLMWXCVB
    :param key: string
    :return: list
    """
    poltab = []

    # Transforme la clé entrée dans l'application en un tableau utilisable pour crypter et décrypter
    for i in range(5):
        poltab.append([])
        for j in range(5):
            letter = key[j + (i * 5)]
            poltab[i].append(letter)
    return poltab


def polybe(text, key, mode):
    print("ezar")


def encrypt(text, key):
    text = utils.process_text(text)
    poltab = __create_poltab(key)
    crypttext = []


