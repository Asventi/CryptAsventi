# main.pyw
import pygubu

import crypt


# Script crée en partie grâce à un tutoriel sur pygubu trouvé sur youtube

class CryptAsventiApp(object):
    def __init__(self, master=None):
        self.method = None
        self.mode = "decrypt"
        self.builder = builder = pygubu.Builder()

        builder.add_from_file("./app.ui")

        self.mainwindow = builder.get_object("mainwindows", master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def setmethod(self, method):
        """
        Recoit un callback lorsqu'une méthode est selectionnée
        """
        self.method = method

    def setmode(self, mode):
        """
        Recoit un callback lorsqu'un mode est selctionné
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
            returntext.set(crypt.rot(text, 2))

        elif self.method == "ROT13":
            returntext.set(crypt.rot(text, 13))

        elif self.method == "Vigenere":
            returntext.set(crypt.vigenere(text, key, self.mode))

        elif self.method == "Polybe":
            returntext.set(crypt.polybe(text, key, self.mode))


# Création de l'application
if __name__ == '__main__':
    app = CryptAsventiApp()
    app.run()
