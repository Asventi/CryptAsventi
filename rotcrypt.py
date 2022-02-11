# rotcrypt.py
import asventicrypt as crpt


# noinspection PyMethodMayBeStatic
class RotCrypt(object):
    """
    C'est une classe qui sert à décrypter et crypter en ROT

    By Asventi
    """

    def __create_dictionnary(self, offset):
        ascii_tab = crpt.chrtab()
        ascii_tab_rot = crpt.decale(ascii_tab, offset)

        rot_dic = {}

        for a, r in zip(ascii_tab, ascii_tab_rot):
            rot_dic[a] = r
        return rot_dic

    def crypt(self, text, offset):
        rot_dic = self.__create_dictionnary(offset)
        crypttext = []
        text = crpt.process_text(text)

        for letter in text:
            if letter in rot_dic:
                crypttext.append(rot_dic[letter])
            else:
                crypttext.append(letter)

        return "".join(crypttext)


