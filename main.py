# On importe sys et getopt pour récupérer les arguments dans la l'invite de commande
import argparse

import rotcrypt
import vigenerecrypt

# On initialise le parser
parser = argparse.ArgumentParser(description="* ** *** CryptAsventi *** ** *")

# On créer les options postionnelles
parser.add_argument("mode", help="Mode to use", choices=["encrypt", "decrypt"])
parser.add_argument("method", help="Encryption/decryption method : rot13, caesar, vegenere, polybe")
parser.add_argument("text", help="Text")

# On récupère les arguments
args = parser.parse_args()

rot = rotcrypt.RotCrypt(13)

vigenere = vigenerecrypt.VigenereCrypt()
vigenere.test()



