# main.py
import pathlib

import pygubu

import rotcrypt
import vigenerecrypt

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "GUI" / "test.ui"


class CryptAsventiApp(object):
    def __init__(self, master=None):
        self.rot = rotcrypt.RotCrypt()
        self.vigenere = vigenerecrypt.VigenereCrypt()
        self.method = None
        self.mode = "decrypt"
        self.builder = builder = pygubu.Builder()

        builder.add_from_file(PROJECT_UI)

        self.mainwindow = builder.get_object("mainwindows", master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def setmethod(self, method):
        self.method = method

    def setmode(self, mode):
        self.mode = mode

    def crypt(self):
        text = self.builder.get_object("entry").get()
        returntext = self.builder.get_variable("returntext")
        key = self.builder.get_object("keyentry").get()

        if self.method == "Caesar":
            returntext.set(self.rot.crypt(text, 2))

        elif self.method == "ROT13":
            returntext.set(self.rot.crypt(text, 13))

        elif self.method == "Vigenere":
            returntext.set(self.vigenere.crypt(text, key, self.mode))


if __name__ == '__main__':
    app = CryptAsventiApp()
    app.run()




