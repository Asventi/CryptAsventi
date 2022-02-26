# vigenerecrypt.py
import asventicrypt as crpt


class VigenereCrypt(object):
    """
    Crypt l'entrée en vigenere
    """

    # Constructeur
    def __init__(self):
        self.vigetab = self.__create_vigetab()

    def __create_vigetab(self):
        """
        Créer un tableau utilisé pour crypter et décrypter en vigenere
        :return: list
        """
        vigetab = [crpt.chrtab()]

        for i in range(1,26):
            line = crpt.decale(vigetab[0], i)  # Utilisation de ma bibliothèque pour décaler les lignes
            vigetab.append(line)  # Ajout des lignes au tableau

        return vigetab

    def crypt(self, text, key, mode):
        """
        Appel la bonne méthode en fonction du mode choisit dans l'applicaiton
        :param text: string
        :param key: string
        :param mode: string
        :return: string
        """
        if mode == "encrypt":
            return self.__encrypt(text, key)
        else:
            return self.__decrypt(text, key)

    def __encrypt(self, text, key):
        """
        Encrypte le text entré en fonction de la clé entrée, la clé doit être sans espaces ni accents
        :param text: string
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
        Decrypte le texte entré en fonction de la clé, la clé ne doit pas avoir d'espaces ni d'accents
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

    def __get_key_adapted(self, key, length, text):
        """
        Transforme la clé entrée en une clé adapté au cryptage du texte entré
        :param key: string
        :param length: int
        :param text: string
        :return: string
        """
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

