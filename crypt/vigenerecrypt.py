# vigenerecrypt.py
from ..utils import crypt_utils as crpt


class VigenereCrypt(object):

    def __init__(self):
        self.vigetab = self.__create_vigetab()

    @staticmethod
    def __create_vigetab():
        """
        :return: talbeau de cyptage en vigenere
        """
        vigetab = [crpt.chrtab()]

        for i in range(1,26):
            line = crpt.decale(vigetab[0], i)
            vigetab.append(line)

        return vigetab

    def crypt(self, text: str, key: str, mode: str):
        """
        :param text: texte à crypter/decrypter
        :param key: clé de decryptage
        :param mode: mode, decrypt ou crypt
        :return: le text crypté/décrypté
        """
        if mode == "encrypt":
            return self.__encrypt(text, key)
        else:
            return self.__decrypt(text, key)

    def __encrypt(self, text: str, key: str):
        """
        :param text: le texte a crypter
        :param key: string
        :return: string
        """

        text = crpt.process_text(text)
        key_adapted = self.__get_key_adapted(key, len(text), text)
        crypttext = []

        for key, letter in zip(key_adapted, text):
            if letter in self.vigetab[0]:
                key_index = self.vigetab[0].index(key)
                letter_index = self.vigetab[0].index(letter)
                letter = self.vigetab[key_index][letter_index]
            crypttext.append(letter)

        return "".join(crypttext)

    def __decrypt(self, text, key):
        """
        :param text: string
        :param key: string
        :return: string
        """
        key_adapted = self.__get_key_adapted(key, len(text), text)
        crypttext = []

        for key, letter in zip(key_adapted, text):
            if letter in self.vigetab[0]:
                key_index = self.vigetab[0].index(key)
                letter = self.vigetab[0][self.vigetab[key_index].index(letter)]
            crypttext.append(letter)
        return "".join(crypttext)

    def __get_key_adapted(self, key: str, length: int, text: str):
        """
        Transforme la clé entrée en une clé adapté au cryptage du texte entré

        :param key: la clé de cryptage/decryptage
        :param length: taille du texte a crypter/decrypter
        :param text: le texte a crypter/decrypter
        :return: string
        """
        key = crpt.process_text(key)
        key = key.upper()
        key_length = len(key)
        key_index = 0
        key_adapted = []

        for i in range(0, length):
            if text[i] in self.vigetab[0]:
                key_adapted.append(key[key_index])
                key_index += 1
                if key_index > key_length - 1:
                    key_index = 0
            else:
                key_adapted.append(" ")
        return "".join(key_adapted)
