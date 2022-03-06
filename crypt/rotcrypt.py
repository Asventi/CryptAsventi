# rotcrypt.py
from ..utils import crypt_utils as crpt


class RotCrypt(object):
    """
    Crypte l'entrée en ROT, sert au ROT13 et au Code Caesar
    """

    def __create_dictionnary(self, offset: int):
        """
        :param offset: décalage de l'alphabet
        :return: retourne un dictionnaire pour crypter et décrypter
        """
        ascii_tab = crpt.chrtab()
        ascii_tab_rot = crpt.decale(ascii_tab, offset)

        rot_dic = {}

        for a, r in zip(ascii_tab, ascii_tab_rot):
            rot_dic[a] = r
        return rot_dic

    def crypt(self, text: str, offset: int):
        """
        :param text: le texte a crypter/décrypter
        :param offset: decalage de l'alphabet
        :return: le texte crypté/décrypté
        """
        rot_dic = self.__create_dictionnary(offset)
        crypttext = []
        text = crpt.process_text(text)

        for letter in text:
            if letter in rot_dic:
                crypttext.append(rot_dic[letter])
            else:
                crypttext.append(letter)

        return "".join(crypttext)


