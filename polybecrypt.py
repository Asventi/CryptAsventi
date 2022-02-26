# polybecrypt.py
import asventicrypt as crpt

class PolybCrypt(object):
    """
    Crypte et décrypte avec le carré de Polybe
    """

    def __create_poltab(self, key):
        """
        Crée le carré de Polybe qui sera utilisé pour crypter et décrypter le tableau doit être entré sous forme
        linéaire, ex 1354919524879531579634894
        :param key: string
        :return: list
        """
        poltab = []

        # Transforme la clé entrée dans l'application en un tableau utilisable pour crypter et décrypter
        for i in range(5):
            poltab.append([])
            for j in range(5):
                num = int(key[j + (i * 5)])
                poltab[i].append(num)
        return poltab

    def encrypt(self, text, key):
        text = crpt.process_text(text)
        poltab = self.__create_poltab(key)
        crypttext =[]



"""
test = PolybCrypt()
print(test.create_poltab("4578946518245635874195286"))
"""
