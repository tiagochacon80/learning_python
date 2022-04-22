from tkinter import Tk, Label, Entry, Button


class Prisme:
    def __init__(self, longueur=2, largeur=1, hauteur=3):
        self.changer_dimensions(longueur, largeur, hauteur)

    def calculer_volume(self):
        return self.longueur * self.largeur * self.hauteur

    def calculer_surface(self):
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)

    def changer_dimensions(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur


class AfficheurDimensions(Tk):
    def __init__(self, prisme):
        super().__init__()
        self.title("Dimensions d'un prisme")
        self.prisme = prisme

        self.creer_widgets()
        self.appliquer_grid()
        self.valeurs_par_defaut()

    def creer_widgets(self):
        self.longueur_label = Label(self, text="Longueur:")
        self.longueur_entry = Entry(self, width=20)
        self.largeur_label = Label(self, text="Largeur:")
        self.largeur_entry = Entry(self, width=20)
        self.hauteur_label = Label(self, text="Hauteur:")
        self.hauteur_entry = Entry(self, width=20)
        self.volume_label = Label(self, text="Volume:")
        self.volume_calcule_label = Label(self)
        self.surface_label = Label(self, text="Surface:")
        self.surface_calculee_label = Label(self)
        self.mise_a_jour_button = Button(self, text="Mettre à jour")
        self.mise_a_jour_button.bind('<Button-1>', self.mettre_a_jour)

    def appliquer_grid(self):
        self.longueur_label.grid(row=0, column=0, padx=20, pady=10)
        self.longueur_entry.grid(row=0, column=1, padx=20, pady=10)
        self.largeur_label.grid(row=1, column=0, padx=20, pady=10)
        self.largeur_entry.grid(row=1, column=1, padx=20, pady=10)
        self.hauteur_label.grid(row=2, column=0, padx=20, pady=10)
        self.hauteur_entry.grid(row=2, column=1, padx=20, pady=10)
        self.volume_label.grid(row=0, column=2, padx=20, pady=10)
        self.volume_calcule_label.grid(row=0, column=3, padx=20, pady=10)
        self.surface_label.grid(row=1, column=2, padx=20, pady=10)
        self.surface_calculee_label.grid(row=1, column=3, padx=20, pady=10)
        self.mise_a_jour_button.grid(row=3, column=1, padx=20, pady=10)

    def mettre_a_jour(self, evt=None):
        self.obtenir_valeurs_inscrites()
        self.calculer_volume_surface()

    def valeurs_par_defaut(self):
        """TODO Q4"""
        self.longueur_entry.insert(0, self.prisme.longueur)
        self.largeur_entry.insert(0, self.prisme.largeur)
        self.hauteur_entry.insert(0, self.prisme.hauteur)

    def calculer_volume_surface(self):
        """TODO Q5"""

    def obtenir_valeurs_inscrites(self):
        """TODO Q6"""


if __name__ == '__main__':
    fenetre = AfficheurDimensions(Prisme())
    fenetre.mainloop()