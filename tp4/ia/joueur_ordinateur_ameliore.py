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
        self.choix = 0

    def strategie(self, choix):
        self.choix = choix

    def best_zone_elargie(self, x, y, case, select, des_apres_vic=0, attaquant_nombre_de_des=0, attaquant_appartenance=""):
        """
        Cette methode permet a l'intelligence artificielle (IA) de determine la meilleur zone d'attaque en attribuant un
        point a un compteur a chaque fois que la case enemie et la case enemie voisine (a cette case) a un un nombre
        de dé inferieur a la case de VOTRE_IA qui attaque.

        La case ayant le plus de point a son compteur represente la meilleur zone pour l'IA.

        Args:
            x, y : Tuple de case.coordonnees
            case: La cases disponibles selectionner l'attaquant
            select : strategie selection (attaque ou defense)
            des_apres_vic : nombre de dé a retire a la case attaquante (simuler le nombre de dé en cas de victoire)
            attaquant_nombre_de_des : Nombre de dé de la case attaquant (strategie_selection_defenseur)
            attaquant_appartenance : Appartenance de la case qui attaque (strategie_selection_defenseur)

        Returns:
            cpte: La somme des point attribue a la case, qui permet de determine la meilleur zone dans les deux cas
                strategie_selection_defenseur et strategie_selection_attaquant

        """
        cpte = 0
        if select == "attaquant":
            # voisins du haut et du bas de case
            for nb in [-1, 1]:

                coor = (x - nb, y)
                if coor[0] > 0 and self.carte.cases.get(coor, 0) != 0:
                    voisin = self.carte.cases.get(coor)
                    if not case.appartenance == voisin.appartenance:
                        if voisin.nombre_de_des() < (case.nombre_de_des() - des_apres_vic):
                            cpte += 1

                # voisin de la gauche et de la droite de case
                coor = (x, y - nb)

                if coor[1] > 0 and self.carte.cases.get(coor, 0) != 0:
                    voisin = self.carte.cases.get(coor)
                    if not case.appartenance == voisin.appartenance:
                        if voisin.nombre_de_des() < (case.nombre_de_des() - des_apres_vic):
                            cpte += 1

        if select == "defense":
            # voisins du haut et du bas de case
            for nb in [-1, 1]:
                coor = (x - nb, y)
                if coor[0] > 0 and self.carte.cases.get(coor, 0) != 0:
                    voisin = self.carte.cases.get(coor)
                    if not attaquant_appartenance == voisin.appartenance.couleur:
                        if voisin.nombre_de_des() < (attaquant_nombre_de_des - des_apres_vic):
                            cpte += 1

            # voisin de la gauche et de la droite de case
                coor = (x, y - nb)
                if coor[1] > 0 and self.carte.cases.get(coor, 0) != 0:
                    voisin = self.carte.cases.get(coor)
                    if not attaquant_appartenance == voisin.appartenance.couleur:
                        if voisin.nombre_de_des() < (attaquant_nombre_de_des - des_apres_vic):
                            cpte += 1

        return cpte

    def best_zone(self, case, select, attaquant_nombre_de_des=0, attaquant_appartenance=""):
        """
        Cette methode cumuler le nombre de point qui determiner la meilleur zone pour la case attaquante
        (strategie_selection_defenseur) ou pour le choix de la case en defense (strategie_selection_defenseur)

        Args:
            case: La cases disponibles selectionner l'attaquant
            select : strategie selection (attaque ou defense)
            attaquant_nombre_de_des : Nombre de dé de la case attaquant (strategie_selection_defenseur)
            attaquant_appartenance : Appartenance de la case qui attaque (strategie_selection_defenseur)

        Returns:
            cpte: La somme des point attribue a la case, qui permet de determine la meilleur zone dans les deux cas
                strategie_selection_defenseur et strategie_selection_attaquant
        """
        cpte = 0
        x = case.coordonnees[0]
        y = case.coordonnees[1]
        if select == "attaquant":
            cpte += self.best_zone_elargie(x, y, case, select, 0, attaquant_nombre_de_des)

            for coor in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                cpte += self.best_zone_elargie(coor[0], coor[1], case, select, 2, attaquant_nombre_de_des)

            for coor in [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]:
                cpte += self.best_zone_elargie(coor[0], coor[1], case, select, 3, attaquant_nombre_de_des)

        if select == "defense":
            cpte += self.best_zone_elargie(x, y, case, select, 1, attaquant_nombre_de_des, attaquant_appartenance)

            for coor in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                cpte += self.best_zone_elargie(coor[0], coor[1], case, select, 2, attaquant_nombre_de_des, attaquant_appartenance)

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
            dict_bestZone[case] = self.best_zone(case, "attaquant")

        if dict_bestZone != {}:
            max_case = max(dict_bestZone, key=dict_bestZone.get)
            ecart_nombre_de_des = self.trouver_nb_des_optimal(cases_disponibles).nombre_de_des() - max_case.nombre_de_des()

            if ecart_nombre_de_des == 0 and (dict_bestZone.get(max_case) >= 2):
                self.strategie(1)
                return max_case

            if ecart_nombre_de_des == 1 and (dict_bestZone.get(max_case) > 4):
                self.strategie(1)
                return max_case

            if ecart_nombre_de_des == 2 and (dict_bestZone.get(max_case) >= 4):
                self.strategie(1)
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
        bool_choix = False
        if self.choix == 1:
            bool_choix = True

            dict_bestZone = {}
            for case in cases_disponibles.values():
                if self.best_zone(case, "defense", case_attaquante.nombre_de_des(), case_attaquante.appartenance.couleur) >= 2:
                    dict_bestZone[case.coordonnees] = case

            if dict_bestZone != {}:
                cases_disponibles = dict_bestZone

        case_defense = self.trouver_nb_des_optimal(
            self.filtrer_nb_des(cases_disponibles,
                    [case_attaquante.nombre_de_des() - 1, case_attaquante.nombre_de_des() - 2]), minimum=bool_choix)

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
                                 range(3, case_attaquante.nombre_de_des())]), minimum=bool_choix)

        if case_defense is not None:
            return case_defense

        # Sinon, l'IA attaque le voisin le plus faible parmi ceux qui sont plus forts qu'elle
        if randint(1, 20) == 1:
            return self.trouver_nb_des_optimal(cases_disponibles, minimum=True)
        else:
            return None
