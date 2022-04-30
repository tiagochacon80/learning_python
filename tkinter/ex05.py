from tkinter import Tk, Label, Entry, Checkbutton, Button


class Fenetre(Tk):
    def __init__(self):
         super().__init__()
         self.title("Division")
         self.label_num = Label(text="Numérateur:")
         self.label_denom = Label(text="Dénominateur:")
         self.entry_num = Entry()
         self.entry_denom = Entry()
         self.checkbutton = Checkbutton(text="Arrondir")
         self.button = Button(text="Calculer")
         self.label_resultat1 = Label(text="Résultat:")
         self.label_resultat2 = Label(text="")
         #self.label_num.grid(row=0, column=0, padx=10, pady=10)
         self.label_denom.grid(row=1, column=0, padx=10, pady=10)
         self.entry_num.grid(row=0, column=1, padx=10, pady=10)
         #self.entry_denom.grid(row=1, column=1, padx=10, pady=10)
         self.checkbutton.grid(row=2, column=0, padx=10, pady=10)
         self.button.grid(row=2, column=1, padx=10, pady=10)
         self.label_resultat1.grid(row=3, column=0, padx=10, pady=10)
         self.label_resultat2.grid(row=3, column=1, padx=10, pady=10)


if __name__ == '__main__':
 fenetre = Fenetre()
 fenetre.mainloop()
