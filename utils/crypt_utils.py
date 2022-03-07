# crypt_utils.py
import unicodedata


def decale(tab: list, offset: int):
    """
    Créer un décalage d'une valeur de offset d'une list

    :param tab: Le tableau à décaler
    :param offset: Le décalage à appliquer
    :return: La list entrée avec le décalage entré
    """

    if len(tab) < 27:  # Si c'est un alphabet avec soit minuscule ou majuscule
        tab_decale = tab[offset:] + tab[:offset]

    else:  # Si c'est un alphabet avec minuscule et majuscule
        tab_decale = tab[offset:26] + tab[:offset] + tab[(offset + 26):] + tab[26:(offset + 26)]

    return tab_decale


def process_text(plaintext: str):
    # Aide d'un tutoriel trouvé sur StackOverflow
    """
    Retourne le texte entré en un texte sans accents

    :param plaintext: string
    :return: string
    """
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', plaintext)
                   if not unicodedata.combining(ch))
    return text


def chrtab():
    """
    :return: renvoie une list de l'alphabet majuscule et minuscule
    """
    tab = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]  # On utilise les list comprehension
    return tab
