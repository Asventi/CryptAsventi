# polybecrypt.py


class PolybCrypt(object):
    """
    Crypte et décrypte avec le carré de Polybe
    """

    def __create_poltab(self, key):
        """
        Crée le carré de Polybe qui sera utilisé pour crypter et décrypter le tableau doit être entré sous forme
        linéaire, ex : AZERTYUIOPQSDFGHJKLMWXCVB
        :param key: string
        :return: list
        """
        poltab = []

        # Transforme la clé entrée dans l'application en un tableau utilisable pour crypter et décrypter
        for i in range(5):
            poltab.append([])
            for j in range(5):
                letter = key[j + (i * 5)]
                poltab[i].append(letter)
        return poltab

    def encrypt(self, text, key):
        text = crpt.process_text(text)
        poltab = self.__create_poltab(key)
        crypttext =[]
        test = "a"
        try:
            return int(test)
        except ValueError:
            print("hey")






test = PolybCrypt()
print(test.encrypt("yaaaaaa","AZERTYUIOPQSDFGHJKLMWXCVB"))
print('ok')

