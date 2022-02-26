# rotcrypt.py
import asventicrypt as crpt


# noinspection PyMethodMayBeStatic
class RotCrypt(object):
    """
    Crypte l'entrée en ROT, sert au ROT13 et au Code Caesar
    """

    def __create_dictionnary(self, offset):
        """
        Sert à créer un dictionnaire pour crypter et décrypter en fonction du décalage
        :param offset: int
        :return: dictionnary
        """
        ascii_tab = crpt.chrtab()
        ascii_tab_rot = crpt.decale(ascii_tab, offset)

        rot_dic = {}

        for a, r in zip(ascii_tab, ascii_tab_rot):
            rot_dic[a] = r
        return rot_dic

    def crypt(self, text, offset):
        """
        Crypte en ROT le texte entré, le chiffre de ROT étant offset
        :param text: string
        :param offset: int
        :return: string
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


