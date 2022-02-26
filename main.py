# main.py

import pygubu

import polybecrypt
import rotcrypt
import vigenerecrypt


# Classe qui sert à la création de l'interface graphique (aide de la documentation de pygububuilder)
class CryptAsventiApp(object):
    def __init__(self, master=None):
        self.rot = rotcrypt.RotCrypt()
        self.vigenere = vigenerecrypt.VigenereCrypt()
        self.polybe = polybecrypt.PolybCrypt()
        self.method = None
        self.mode = "decrypt"
        self.builder = builder = pygubu.Builder()

        builder.add_from_file("./test.ui")

        self.mainwindow = builder.get_object("mainwindows", master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def setmethod(self, method):
        """
        Recoit un callback lorsqu'un mode est selectionné
        :param method: string
        """
        self.method = method

    def setmode(self, mode):
        """
        Recoit un callback lorsqu'un mode est selctionné
        :param mode: string
        """
        self.mode = mode

    def crypt(self):
        """
        Recoit un callback lorsque que le bouton OK est pressé
        Méthode qui sert à appeler les bonnes fonctions en fonction du mode choisition
        Et retourne dans la boîte de texte le texte crypté
        """
        text = self.builder.get_object("entry").get()
        returntext = self.builder.get_variable("returntext")
        key = self.builder.get_object("keyentry").get()

        if self.method == "Caesar":
            returntext.set(self.rot.crypt(text, 2))

        elif self.method == "ROT13":
            returntext.set(self.rot.crypt(text, 13))

        elif self.method == "Vigenere":
            returntext.set(self.vigenere.crypt(text, key, self.mode))

        elif self.method == "Polybe":
            print("ok")
            #returntext.set(self.polybe.crypt(text, key, self.mode))


# Création de l'application
if __name__ == '__main__':
    app = CryptAsventiApp()
    app.run()
