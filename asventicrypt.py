import unicodedata


"""
Petite bibliothèque d'utilitaires pour mon projet

By Asventi
"""


def decale(tab, offset):
    if len(tab) < 27:
        tab_decale = tab[offset:] + tab[:offset]
    else:
        tab_decale = tab[offset:26] + tab[:offset] + tab[(offset+26):] + tab[26:(offset+26)]
    return tab_decale


def process_text(plaintext):
    # Transforme le texte en un texte sans accents (Un tutoriel à été utilisé pour réaliser cette fonction)
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', plaintext)
                   if not unicodedata.combining(ch))
    return text


def chrtab():
    tab = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]
    return tab
