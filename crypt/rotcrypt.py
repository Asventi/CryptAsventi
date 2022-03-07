# rotcrypt.py
import utils


def __create_dictionnary(offset: int):
    """
    Créer un dictionnaire servant au cryptage avec un alphabet décalé

    :param offset: décalage de l'alphabet
    :return: retourne un dictionnaire pour crypter et décrypter
    """
    ascii_tab = utils.chrtab()
    ascii_tab_rot = utils.decale(ascii_tab, offset)  # On utilise

    rot_dic = {}

    for a, r in zip(ascii_tab, ascii_tab_rot):
        rot_dic[a] = r

    return rot_dic


def rot(text: str, offset: int):
    """
    Crypte et décrypte en ROT

    :param text: le texte à crypter/décrypter
    :param offset: decalage de l'alphabet
    :return: le texte crypté/décrypté
    """
    rot_dic = __create_dictionnary(offset)
    crypttext = []
    text = utils.process_text(text)

    for letter in text:
        if letter in rot_dic:
            crypttext.append(rot_dic[letter])

        else:
            crypttext.append(letter)

    return "".join(crypttext)
