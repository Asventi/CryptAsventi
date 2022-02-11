
# noinspection PyMethodMayBeStatic
class RotCrypt(object):
    """
    C'est une classe qui sert à décrypter et crypter en ROT

    By Asventi
    """

    def __init__(self, offset):
        self.rot_dic = self.__create_dictionnary(offset)

    def __create_dictionnary(self, offset):
        ascii_tab = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]

        ascii_tab_rot = ascii_tab[offset:26] + ascii_tab[:offset] + ascii_tab[(offset+26):] + ascii_tab[26:(offset+26)]
        rot_dic = {}

        for a, r in zip(ascii_tab, ascii_tab_rot):
            rot_dic[a] = r
        return rot_dic

    def crypt(self, text):
        crypttext = []

        for letter in text:
            if letter in self.rot_dic:
                crypttext.append(self.rot_dic[letter])
            else:
                crypttext.append(letter)

        return "".join(crypttext)
