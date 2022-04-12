from tkinter import Tk, Frame, Button
fenetre = Tk()
fenetre.title("grid()")

cadre = Frame(fenetre)
cadre.grid(padx=10, pady=10)

for i in range(3):
    for j in range(3):
        t = "({},{})".format(i, j)
        b = Button(cadre, text=t, padx=1, pady=3)
        b.grid(row=i, column=j, padx=5, pady=7)

fenetre.mainloop()