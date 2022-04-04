from tkinter import *
import os

c=os.path.dirname(__file__)
nomFichier=c+"\\noms.txt"

def impDados():
    fichier=open(nomFichier,"a")    
    fichier.write("Nom...:%s" % vnom.get())
    fichier.write("\nTelephone:%s" % vtelephone.get())
    fichier.write("\nE-mail:%s" % vemail.get())
    fichier.write("\nCommentaires:%s" % vcommentaires.get("1.0",END))
    fichier.write("\n\n")
    fichier.close()

app=Tk()
app.title("")
app.geometry("400x300")
app.configure(background="#dde")

Label(app,text="Nom",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnom=Entry(app)
vnom.place(x=10,y=30,width=200,height=20)

Label(app,text="Telephone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vtelephone=Entry(app)
vtelephone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail=Entry(app)
vemail.place(x=10,y=130,width=250,height=20)

Label(app,text="Commentaires",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vcommentaires=Text(app)
vcommentaires.place(x=10,y=190,width=250,height=60)

Button(app,text="Enregistrer",command=impDados).place(x=10,y=270,width=100,height=20)


app.mainloop()