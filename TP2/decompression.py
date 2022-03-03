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

    return chaine.replace(symbole, paire)



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

    SYMBOLES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in SYMBOLES[::-1]:
        if i in dictionnaire_paires:
            chaine = remplacer_symbole_par_paire(chaine, dictionnaire_paires[i], i)

    return chaine


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
    chaine_compressee, dictionnaire_paires = lire_fichier_compresse(fichier_compresse)
    chaine_decompressee = decompression_par_paires(chaine_compressee, dictionnaire_paires)
    ecrire_fichier_decompresse(fichier_decompresse, chaine_decompressee)
    print("Décompression complétée!")


if __name__ == '__main__':
    assert remplacer_symbole_par_paire("haXhaXX", "hi", "X") == "hahihahihi"
    assert decompression_par_paires("E", {"A": "hi", "B": "ha", "C": "BA", "D": "CC", "E": "DA"}) == "hahihahihi"
