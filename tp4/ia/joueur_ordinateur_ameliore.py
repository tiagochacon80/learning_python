"""
Ce module contient la classe JoueurOrdinateurAmeliore.
À la base, ce joueur hérite de JoueurOrdinateur, et n'est donc qu'un ordinateur ayant
la même stratégie d'intelligence artificielle.

Vous devez redéfinir les méthodes strategie_selection_attaquant et strategie_selection_defenseur
pour rendre cette intelligence plus fûtée que l'intelligence originale.

Attention, une fois les méthodes décommentées, elles effaceront les méthodes du même nom
de JoueurOrdinateur.

Des idées de changement à apporter sont disponibles dans l'énoncé.
"""
import operator
from random import randint

from guerre_des_des_tp3.joueur_ordinateur import JoueurOrdinateur
from guerre_des_des_tp3.carte import Carte


class JoueurOrdinateurAmeliore(JoueurOrdinateur):
    def __init__(self, couleur, carte):
        """
        Constructeur de la classe JoueurOrdinateurAmeliore

        Args:
            couleur (str): La couleur du joueur. Cela lui sert de nom.
            carte (Carte): La totalité de la carte, pour vous aider à prendre
                des décisions plus globales
        """
        super().__init__(couleur)
        self.carte = carte

    def best_zone_elargie(self, x, y, case):
        cpte = 0

        # voisins du haut et du bas de case
        for nb in [-1, 1]:

            coor = (x-nb, y)
            if coor[0] > 0 and self.carte.cases.get(coor, 0) != 0:
                voisin = self.carte.cases.get(coor)
                if voisin.nombre_de_des() < case.nombre_de_des():
                    if not case.appartenance == voisin.appartenance:
                        cpte += 1

            # voisin de la gauche et de la droite de case
            coor = (x, y-nb)

            if coor[1] > 0 and self.carte.cases.get(coor, 0) != 0:
                voisin = self.carte.cases.get(coor)
                if voisin.nombre_de_des() < case.nombre_de_des():
                    if not case.appartenance == voisin.appartenance:
                        cpte += 1

        return cpte

    def best_zone(self, case):
        cpte = 0
        x = case.coordonnees[0]
        y = case.coordonnees[1]
        for coor in [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            cpte += self.best_zone_elargie(coor[0], coor[1], case)

        return cpte

    def strategie_selection_attaquant(self, cases_disponibles):
        """
        Cette méthode implémente l'intelligence artificielle (IA) permettant de sélectionner
        un attaquant.

        Args:
            cases_disponibles (dict): Les cases disponibles pour attaque

        Returns:
            Case: La case sélectionnée par l'IA. None si elle arrête son tour.
        """
        # L'IA a une chance sur 20 d'arrêter son tour
        if randint(1, 20) == 1:
            return None

        # On determiner la zone la plus avantageuse pour attaquer
        dict_bestZone = {}
        for case in cases_disponibles.values():
            dict_bestZone[case] = self.best_zone(case)

        if dict_bestZone != {}:
            max_case = max(dict_bestZone, key=dict_bestZone.get)
            ecart_nombre_de_des = self.trouver_nb_des_optimal(cases_disponibles).nombre_de_des() - max_case.nombre_de_des()

            if ecart_nombre_de_des in [0, 1, 2, 3, 4]:
                 return max_case

        return self.trouver_nb_des_optimal(cases_disponibles)

    def strategie_selection_defenseur(self, cases_disponibles, case_attaquante):
        """
        Cette méthode implémente l'intelligence artificielle (IA) permettant de sélectionner
        un défenseur.

        Args:
            cases_disponibles (dict): Les cases disponibles pour attaque
            case_attaquante (Case): La case qui attaque

        Returns:
            Case: La case sélectionnée par l'IA. None si elle retourne à la phase de
            sélection de l'attaquant.
        """

        # Si des voisins ont 1 ou 2 dés de moins, l'IA attaque le plus faible d'entre eux
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles,
                                [case_attaquante.nombre_de_des() - 1, case_attaquante.nombre_de_des() - 2]), minimum=True)

        if case_defense is not None:
            return case_defense

        # Sinon, si un voisin a autant de dés que l'IA, elle l'attaque
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles, [case_attaquante.nombre_de_des()]))

        if case_defense is not None:
            return case_defense

        # Sinon, si un voisin a au moins 3 dés de moins que l'IA, elle attaque le plus fort d'entre eux
        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles,
                                [case_attaquante.nombre_de_des() - i for i in
                                 range(3, case_attaquante.nombre_de_des())]))

        if case_defense is not None:
            return case_defense

        # Sinon, l'IA attaque le voisin le plus faible parmi ceux qui sont plus forts qu'elle
        if randint(1, 10) == 1:
            return self.trouver_nb_des_optimal(cases_disponibles, minimum=True)
        else:
            return None