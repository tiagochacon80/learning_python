"""
Contient la classe Joueur, qui correspond à une entité qui joue au jeu, que ce soit un humain
ou un ordinateur.
"""

from random import choice

from afficheur import afficher
from de import De

# Cette constante fixe le nombre de dés à répartir sur les cases d'un joueur en début de partie. De base,
# toutes les cases ont un dé, mais on y ajoute aussi ce nombre de dés réparti sur toutes les cases.
DES_SURPLUS_INITIAUX = 10


class Joueur:
    def __init__(self, couleur, type_joueur):
        """
        Constructeur de la classe Joueur

        Args:
            couleur (str): La couleur du joueur. Cela lui sert de nom.
            type_joueur (str): Le type de joueur, pour l'affichage.
        """
        self.couleur = couleur
        self.type_joueur = type_joueur
        self.des_en_surplus = [De() for _ in range(DES_SURPLUS_INITIAUX)]

    def selectionner_attaquant(self, carte):
        """
        Cette méthode permet de choisir une case en fonction de la carte
        (Carte.cases_disponibles_pour_attaque) et de la stratégie de sélection d'attaquant
        (Joueur.strategie_selection_attaquant). Si la stratégie retourne une case, la
        case est alors sélectionnée pour attaque (Case.selectionner_pour_attaque).

        Args:
            carte (Carte): La carte du jeu

        Returns:
            Case: La case sélectionnée pour attaque. None si la stratégie retourne None
        """
        # VOTRE CODE ICI

    def selectionner_defenseur(self, carte, case_attaquante):
        """
        Cette méthode permet de choisir une case en fonction de la carte
        (Carte.cases_disponibles_pour_defense) et de la
        stratégie de sélection de défenseur (Joueur.strategie_selection_defenseur).
        Si la stratégie retourne une case, la case est alors sélectionnée
        pour défense (Case.selectionner_pour_defense).

        Args:
            carte (Carte): La carte du jeu
            case_attaquante (Case): La case qui attaquera ce défenseur

        Returns:
            Case: La case sélectionnée pour défense. None si la stratégie retourne None
        """
        # VOTRE CODE ICI

    def strategie_selection_attaquant(self, cases_disponibles):
        raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

    def strategie_selection_defenseur(self, cases_disponibles, case_attaquante):
        raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

    def ajouter_n_des(self, nouveaux_des):
        """
        Cette méthode ajoute les nouveaux dés aux dés en surplus.

        Args:
            nouveaux_des (list): La liste de dés à ajouter.
        """
        # VOTRE CODE ICI

    def distribuer_surplus(self, carte):
        """
        Cette méthode distribue les dés en surplus à travers les cases
        non pleines appartenant au joueur.

        Args:
            carte (Carte): La carte du jeu
        """
        cases_non_pleines = carte.obtenir_cases_non_pleines(self)
        while len(cases_non_pleines) > 0 and len(self.des_en_surplus) > 0:
            self.attribuer_de_case_au_hasard(list(cases_non_pleines.values()))
            cases_non_pleines = carte.obtenir_cases_non_pleines(self)

    def attribuer_de_case_au_hasard(self, cases_non_pleines):
        """
        Cette méthode pige une case au hasard (random.choice), retire un dé
        des dés en surplus et l'ajoute à la case pigée (Case.ajouter_un_de).

        Args:
            cases_non_pleines (list): La liste de cases desquelles on pige la case.

        """
        # VOTRE CODE ICI

    def est_elimine(self, carte):
        """
        Cette méthode indique si le joueur est éliminé, ce qui est le cas lorsque
        aucune case ne lui appartient (Carte.obtenir_cases_joueur).

        Args:
            carte (Carte): La carte du jeu

        Returns:
            bool: True si la carte ne contient aucune case appartenant au joueur, False sinon.

        """
        # VOTRE CODE ICI

    def afficher_information(self):
        """
        Cette méthode affiche (afficheur.afficher) le type du joueur colorisé avec sa couleur.
        """
        # VOTRE CODE ICI

    def afficher_tour(self):
        """
        Cette méthode affiche (afficheur.afficher) que c'est le tour de ce joueur, avec son nom (couleur) et le
        nombre de dés en surplus, le tout colorisé avec sa couleur.
        """
        # VOTRE CODE ICI

    def afficher_victoire(self):
        """
        Cette méthode affiche (afficheur.afficher) la victoire du joueur,
        avec son nom (couleur), colorisé avec sa couleur.
        """
        # VOTRE CODE ICI
