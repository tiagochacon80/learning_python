from tkinter import Tk, messagebox

try:
    cases = {}
    fichier = open("fichier.txt", 'r')
    for h, line in enumerate(fichier):
        for l, car in enumerate(line):
            if car == ".":
                cases[(h, l)] = (h, l)




    print(cases)
except FileNotFoundError:
    messagebox.showerror("Erreur", "file not exist")