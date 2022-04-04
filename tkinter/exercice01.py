from tkinter import *

app=Tk() #element de la classe
app.title("Et c’est reparti !")
app.geometry("300x200")
app.configure(background="#008")

txt1=Label(app,text="Introduction a la programmation",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=200,height=20)

vtxt="Modulo Tkinter"
vbg="#ff0"
vfg="#000"
txt2=Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True)

app.mainloop()