"""
Contient la classe Case, qui correspond à une case du jeu.
"""

from afficheur import afficher
from de import De

# Cette constante fixe le nombre maximal de dés dans une case
MAX_DES_PAR_CASE = 8

# Ce dictionnaire indique le format d'affichage associé à chaque mode qu'une case peut avoir
FORMATS = {
    'attente': '[ {} ]',
    'attaque': 'X {} X',
    'defense': '< {} >'
}


class Case:
    def __init__(self, coordonnees):
        """
        Constructeur de la classe Case

        Args:
            coordonnees (tuple): Les coordonnées (x, y) de la case

        """
        self.coordonnees = coordonnees
        self.appartenance = None
        self.des = [De()]
        self.mode = 'attente'
        self.voisins = []

    def definir_appartenance(self, joueur):
        """
        Cette méthode définit l'appartenance de cette case au joueur en paramètre

        Args:
            joueur (Joueur): Le joueur
        """
        # VOTRE CODE ICI

    def definir_voisins(self, voisins):
        """
        Cette méthode définit les voisins de la case comme étant ceux en argument

        Args:
            voisins (list): La liste des voisins à donner à la case
        """
        # VOTRE CODE ICI

    def nombre_de_des(self):
        """
        Cette méthode retourne le nombre de dés présents sur la case

        Returns:
            int: Le nombre de dés
        """
        # VOTRE CODE ICI

    def ajouter_un_de(self, de):
        """
        Cette méthode ajoute le dé en paramètre à la liste de dés de la case. Si la
        case est pleine, on lance une ValueError et on n'ajoute pas le dé.

        Args:
            de (De): Le dé à ajouter
        """
        if self.est_pleine():
            raise ValueError("On ne peut ajouter davantage de dés!")
        else:
            self.des.append(de)

    def remplacer_des(self, des):
        """
        Cette méthode remplace tous les dés de la case par ceux en argument.

        Args:
            des (list): Les nouveaux dés
        """
        # VOTRE CODE ICI

    def selectionner_pour_attaque(self):
        """
        Cette méthode change le mode de la case pour le mode 'attaque'
        """
        # VOTRE CODE ICI

    def selectionner_pour_defense(self):
        """
        Cette méthode change le mode de la case pour le mode 'defense'
        """
        # VOTRE CODE ICI

    def deselectionner(self):
        """
        Cette méthode change le mode de la case pour le mode 'attente'
        """
        # VOTRE CODE ICI

    def est_pleine(self):
        """
        Cette méthode indique si le nombre de dés dans la case est égal au nombre maximal
        de dés par case

        Returns:
            bool: True si le nombre de dés est égal au maximum, False sinon
        """
        # VOTRE CODE ICI

    def lancer_des(self):
        """
        Cette méthode lance chacun des dés (De.lancer) et en retourne la somme.
        Il faut afficher également cette somme (affichage.afficher).

        Returns:
            int: La somme des dés
        """
        # VOTRE CODE ICI

    def afficher(self):
        """
        Cette méthode affiche la case selon le format correspondant à son mode
        et la couleur du joueur auquel elle appartient.
        """

        texte_case = FORMATS[self.mode].format(self.nombre_de_des())
        if self.appartenance is not None:
            afficher(texte_case, couleur=self.appartenance.couleur, end='')
        else:
            afficher(texte_case, end='')
