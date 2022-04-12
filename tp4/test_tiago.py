from tkinter import Tk, Button


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class MyWindow(Tk):

    def __init__(self):
        # On appelle le constructeur parent
        super().__init__()

        # Pour que la grille occupe 100% de la fenêtre, il faut que tkinter
        # connaisse à l'avance le nombre de lignes et le nombre de colonnes.
        # Le paramètre weight indique que chaque colonne (et chaque ligne)
        # à le même poids. L'une ne prendra pas l'avantage sur l'autre.
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # On place les 4 boutons dans chacune des cases
        button1 = Button(self, text="Button 1")
        button1.grid(column=0, row=0)

        button2 = Button(self, text="Button 2")
        button2.grid(column=1, row=0)

        button3 = Button(self, text="Button 3")
        button3.grid(column=0, row=1)

        button4 = Button(self, text="Button 4")
        button4.grid(column=1, row=1)

        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Positionnement de widgets via grid")


# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()