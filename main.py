# On importe sys et getopt pour récupérer les arguments dans la l'invite de commande
import argparse
import string


# On initialise le parser
parser = argparse.ArgumentParser(description="* ** *** CryptAsventi *** ** *")

# On créer les options postionnelles
parser.add_argument("mode", help="Mode to use", choices=["encrypt", "decrypt"])
parser.add_argument("method", help="Encryption/decryption method : rot13, caesar, vegenere, polybe")
parser.add_argument("text", help="Text")

# On récupère les arguments
args = parser.parse_args()


def Rot(text, x):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    trans = str.maketrans(lower_case + upper_case, lower_case[x:] + lower_case[:x] + upper_case[x:] + upper_case[:x])
    return str.translate(text, trans)


print(Rot("coucou les musulmans", 13))

