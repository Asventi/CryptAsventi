# crypt_utils.py
import unicodedata


def decale(tab, offset):
    """
    Créer un décalage d'une valeur de offset d'une list de string
    :param tab: list
    :param offset: int
    :return: list
    """

    if len(tab) < 27:
        tab_decale = tab[offset:] + tab[:offset]
    else:
        tab_decale = tab[offset:26] + tab[:offset] + tab[(offset + 26):] + tab[26:(offset + 26)]
    return tab_decale


def process_text(plaintext):
    # Aide d'un tutoriel trouvé sur StackOverflow
    """
    Transforme le texte entré en un texte sans accents
    :param plaintext: string
    :return: string
    """
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', plaintext)
                   if not unicodedata.combining(ch))
    return text


def chrtab():
    """
    Crée et renvoie une list de l'alphabet majuscule et minuscule.
    :return: list
    """
    tab = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]
    return tab
