"""
Module contenant les fonctions permettant d'effectuer la compression
"""

from interaction_fichiers_texte import lire_fichier_brut, ecrire_fichier_compresse

SYMBOLES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def trouver_paire_la_plus_frequente(chaine):
    """
    Cette fonction trouve la paire de symboles subséquents la plus commune dans
    la chaîne de caractères en argument.

    Attention: Mis à part les symboles aux extrémités, chaque symbole fait partie de
    deux paires de symboles. Indice: dans une chaîne de n symboles, il y a n-1 paires.

    Exemple:
    hahihahihi -> ha: 2, ah: 2, hi: 3, ih: 2
    Donc la fonction retournerait "hi"

    Args:
        chaine (str): La chaîne de caractère à analyser

    Returns:
        str: La paire de symboles la plus fréquente dans chaine

    """

    # Votre code ici
    mon_dico = {}
    for i in range(len(chaine)-1):
        pair = chaine[i:i+2]

        if pair in mon_dico:
            mon_dico[pair] += 1
        else:
            mon_dico[pair] = 1

    max_conteur = 0
    max_pair = None
    for pair, conteur in mon_dico.items():
        if conteur > max_conteur:
            max_conteur = conteur
            max_pair = pair

    return max_pair



def remplacer_paire_par_symbole(chaine, paire, symbole):
    """
    Cette fonction remplace toutes les occurences de la paire dans la chaine
    par le symbole.

    Exemple:
    chaine=hahihahihi, paire=hi, symbole=X
    Donc la fonction retournerait "haXhaXX"

    Args:
        chaine (str): La chaîne où effectuer des remplacements
        paire (str): La paire à remplacer
        symbole (str): Le symbole à mettre au lieu de la paire

    Returns:
        str: La chaîne suite aux remplacements

    """

    # Votre code ici


def afficher_progression(ratio):
    """
    Cette fonction affiche une barre de progression correspondant à la fraction
    reçue en argument.

    Args:
        ratio (float): La fraction de progression, entre 0 et 1.
    """

    print("\rProgression: [{0:50s}] {1:.1f}%".format('#' * int(ratio * 50), ratio * 100),
          end="", flush=True)


def compression_par_paires(chaine):
    """
    Cette fonction effectue toute la compression sur la chaîne en argument.
    Pour chaque symbole (voir la variable globale symboles), on
    trouve la paire la plus fréquente, on l'ajoute à un dictionnaire associant le symbole
    avec la paire, et on remplace la paire par le symbole dans la chaîne.
    La fonction doit arrêter s'il n'y a plus de symboles disponibles OU si la chaîne ne contient plus
    qu'un seul symbole.
    N'oubliez pas de réutiliser les fonctions programmées ci-haut.

    Facultatif: affichez la progression à chaque itération en appelant la fonction afficher_progression.

    Args:
        chaine (str): La chaîne à compresser.

    Returns:
        str: La chaîne compressée
        dict: Le dictionnaire de paires.

    """

    # Votre code ici


def compresser(fichier_original, fichier_compresse):
    """
    Cette fonction lit le fichier original, le compresse et écrit le résultat
    dans le fichier compressé.

    Note: cette fonction devrait principalement appeler d'autres fonctions

    Args:
        fichier_original (str): Le nom du fichier où lire le contenu original
        fichier_compresse (str): Le nom du fichier où écrire le contenu compressé
    """
    print("Compression en cours...")
    # Votre code ici
    print("Compression complétée!")


if __name__ == '__main__':
    chaine_test = "hahihahihi"
    assert trouver_paire_la_plus_frequente(chaine_test) == "hi"
    assert remplacer_paire_par_symbole(chaine_test, "hi", "X") == "haXhaXX"
    assert compression_par_paires(chaine_test) == \
           ("E", {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"})
