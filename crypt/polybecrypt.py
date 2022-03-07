# polybecrypt.py
import utils

poltab = []
chrtab = utils.chrtab()
numtab = [str(x) for x in range(1,10)]


def polybe(text: str, key: str, mode: str):
    """
    Choisit la bon mode de cryptage en fonction du mode, crypte en Polybe

    :param text: Le texte à crypter/décrypter
    :param key: Clé de cryptage/décryptage
    :param mode: Mode, "encrypt" ou "decrypt"
    :return: Le text crypter/décrypter
    """

    key = key.upper()
    global poltab  # On utilise la variable globale pour qu'elle soit accessible depuis toutes les fonctions
    poltab = __create_poltab(key)

    text = utils.process_text(text)
    text = text.upper()

    if mode == "encrypt":
        return __encrypt(text)
    else:
        return __decrypt(text)


def __encrypt(text: str):
    """
    Crypte le texte entré en Polybe

    :param text: Texte à crypter
    :return: Texte crypté
    """

    text = text.upper()
    crypttext = []

    for letter in text:
        if letter in chrtab:  # On vérifie bien que la lettre est bien cryptable, sinon on l'ajoute sans cryptage
            x, y = __index_letter(letter)
            letter = str(x + 1) + str(y + 1)  # On ajoute 1, car x et y sont les coordoonées en commencant par 0

        crypttext.append(letter)

    return "".join(crypttext)


def __decrypt(text: str):
    """
    Décrypte le texte entré en Polybe

    :param text: Texte à décrypter
    :return: Texte décrypté
    """

    crypttext = []
    pair = ""

    for num in text:
        if num in numtab:  # On vérifie que le chiffre est bien un chiffre pour éviter les erreurs
            pair += num

            if len(pair) == 2:  # Si la paire est complète on l'ajoute à la phrase décryptée
                decrypt_letter = poltab[int(pair[0])-1][int(pair[1])-1]  # Les index d'une list commencent par 0 donc -1
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

    for i, line in enumerate(poltab):  # On récupère la ligne et son index grâce à enumerate
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
            letter = key[j + (i * 5)]  # Ici on fait i*5 pour prendre les lettres une ligne plus loin à chaque fois
            poltab[i].append(letter)

    return poltab

