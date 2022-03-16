import random

def jouer():

    imprime_mots_de_bienvenu()
    mots_secret = charge_le_mot_secret()
    lettres_trouve = initialise_lettres_trouvees(mots_secret)
    print(lettres_trouve)

    enforcou = False
    trouve = False
    erreurs = 0

    while not enforcou and not trouve:

        chute = demande_utilisateur()

        if chute in mots_secret:
            ecrit_bonne_tentativa(chute, lettres_trouve, mots_secret)
        else:
            erreurs += 1
            dessine_pendu(erreurs)

        enforcou = erreurs == 7
        trouve = "_" not in lettres_trouve
        print(lettres_trouve)

    if trouve:
        affiche_message_gagnant()
    else:
        affiche_message_perdant(mots_secret)


def demande_utilisateur():
    chute = input("Entrez une lettre: ")
    chute = chute.strip().upper()
    return chute

def ecrit_bonne_tentativa(chute, lettres_trouve, mots_secret):
    position = 0
    for lettre in mots_secret:
        if chute == lettre:
            lettres_trouve[position] = lettre
        position += 1

def initialise_lettres_trouvees(mots):
    return ["_" for lettre in mots]

def imprime_mots_de_bienvenu():
    print("*" * 30)
    print("***Bienvenu au jeu da forca***")
    print("*" * 30)

def charge_le_mot_secret():
    archive = open("mots.txt", "r")
    mots = []

    for line in archive:
        line = line.strip()
        mots.append(line)

    archive.close()

    numero = random.randrange(0, len(mots))
    mots_secret = mots[numero].upper()
    return mots_secret

def dessine_pendu(erreurs):
    print("  _______     ")
    print(" |/      |    ")

    if(erreurs == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erreurs == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erreurs == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erreurs == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erreurs == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erreurs == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erreurs == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def affiche_message_gagnant():
        print("Félicitation, vous avez gagné!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def affiche_message_perdant(mots_secret):
        print("Vous avez perdu, vous avez été pendu!")
        print(f"le mot secret était {mots_secret}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

if(__name__== "__main__"):
    jouer()
