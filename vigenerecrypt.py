# vigenerecrypt.py
import asventicrypt as crpt


# noinspection PyMethodMayBeStatic
class VigenereCrypt(object):
    """
    C'est une classe qui sert à crypter et décrypter en VigenereCryp

    By Asventi
    """

    # Constructeur
    def __init__(self):
        self.vigetab = self.__create_vigetab()

    # Création du tableau vigenere pour gérer plus facile le cryptage et le décryptage
    def __create_vigetab(self):
        vigetab = [crpt.chrtab()]  # Création de la première ligne du tableau grâce à ma bibliothèque

        for i in range(1,26):
            line = crpt.decale(vigetab[0], i)  # Utilisation de ma bibliothèque pour décaler les lignes
            vigetab.append(line)  # Ajout des lignes au tableau

        return vigetab

    def crypt(self, text, key, mode):
        if mode == "encrypt":
            return self.encrypt(text, key)
        else:
            print('en cours')

    def encrypt(self, text, key):
        """
        Encryption de du texte entré en paramètre avec la clé
        La clé devant être en majuscule
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

    def __get_key_adapted(self, key, length, text):

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

