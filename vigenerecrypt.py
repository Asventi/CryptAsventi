# noinspection PyMethodMayBeStatic
class VigenereCrypt(object):
    """
    C'est une classe qui sert à crypter et décrypter en VigenereCryp

    By Asventi
    """

    def __init__(self):
        self.vigetab = self.__create_vigetab()

    def __create_vigetab(self):
        vigetab = []

        for i in range(0,26):
            offset = 0
            line = []

            for k in range(0,26):
                line.append(chr(i + 65 + offset))
                offset += 1

            vigetab.append(line)

        return vigetab

    def test(self):
        print(self.vigetab)