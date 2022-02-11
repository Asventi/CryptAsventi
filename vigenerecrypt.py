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

    def test(self):
        print("hey")
