def jouer():
    print("*"*30)
    print("***Bienvenu au jeu da forca***")
    print("*"*30)

    mots_secret = "banana".upper()
    lettres_trouve = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    trouve = False
    erreurs = 0

    print(lettres_trouve)

    while not enforcou and not trouve:

        chute = input("Entrez une lettre: ")
        chute = chute.strip().upper()

        if chute in mots_secret:
            position = 0
            for lettre in mots_secret:
                if chute == lettre:
                    lettres_trouve[position] = lettre
                position += 1
        else:
            erreurs += 1
            print(f"Erreur, il vous manque {6 - erreurs} tentatives")

        enforcou = erreurs == 6
        trouve = "_" not in lettres_trouve
        print(lettres_trouve)

    if trouve:
        print("Vous avez gagné!")
    else:
        print("Vous avez perdu!")
    print("Game over")

if(__name__== "__main__"):
    jouer()

