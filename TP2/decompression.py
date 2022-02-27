"""
Module contenant les fonctions permettant d'effectuer la décompression
"""

from compression import SYMBOLES
from interaction_fichiers_texte import lire_fichier_compresse, ecrire_fichier_decompresse


def remplacer_symbole_par_paire(chaine, paire, symbole):
    """
    Cette fonction remplace toutes les occurences du symbole par la paire en argument.

    Exemple:
    chaine=haXhaXX, paire=hi, symbole=X
    Donc la fonction retournerait "hahihahihi"

    Args:
        chaine (str): La chaîne où effectuer des remplacements
        paire (str): La paire à mettre au lieu du symbole
        symbole (str): Le symbole à remplacer

    Returns:
        str: La chaîne suite aux remplacements

    """

    chaine = chaine.replace(symbole, paire)
    return chaine


def decompression_par_paires(chaine, dictionnaire_paires):
    """
        Cette fonction effectue toute la décompression sur la chaîne en argument,
        en utilisant le dictionnaire de paires.
        Parcourir chaque symbole (importez la variable globale symboles du fichier compression)
        en ordre inverse, et remplacer toutes les occurences de ce symbole par la paire correspondante.
        N'oubliez pas de réutiliser la fonction programmée ci-haut.

        Args:
            chaine (str): La chaîne compressée.
            dictionnaire_paires (dict): Le dictionnaire de paires.

        Returns:
            str: La chaîne décompressée.
        """
    dico_paire = list(dictionnaire_paires.keys())
    val_dic = list(dictionnaire_paires.values())

    for s in SYMBOLES[::-1]:
        if chaine.count(s) > 0:
            position = dico_paire.index(s)
            chaine = remplacer_symbole_par_paire(chaine, val_dic[position], s)


def decompresser(fichier_compresse, fichier_decompresse):
    """
    Cette fonction lit le fichier compressé, le décompresse et écrit le résultat
    dans le fichier décompressé.

    Note: cette fonction devrait principalement appeler d'autres fonctions

    Args:
        fichier_compresse (str): Le nom du fichier où lire le contenu compressé
        fichier_decompresse (str): Le nom du fichier où écrire le contenu décompressé
    """

    print("Décompression en cours...")
    # Votre code ici
    print("Décompression complétée!")


if __name__ == '__main__':
    assert remplacer_symbole_par_paire("haXhaXX", "hi", "X") == "hahihahihi"
    assert decompression_par_paires("E", {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"}) == "hahihahihi"
