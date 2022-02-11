import asventicrypt as crpt


# noinspection PyMethodMayBeStatic
class RotCrypt(object):
    """
    C'est une classe qui sert à décrypter et crypter en ROT

    By Asventi
    """

    def __init__(self, offset):
        self.rot_dic = self.__create_dictionnary(offset)

    def __create_dictionnary(self, offset):
        ascii_tab = crpt.chrtab()
        ascii_tab_rot = crpt.decale(ascii_tab, offset)

        rot_dic = {}

        for a, r in zip(ascii_tab, ascii_tab_rot):
            rot_dic[a] = r
        return rot_dic

    def crypt(self, text):
        crypttext = []
        text = crpt.process_text(text)

        for letter in text:
            if letter in self.rot_dic:
                crypttext.append(self.rot_dic[letter])
            else:
                crypttext.append(letter)

        return "".join(crypttext)


