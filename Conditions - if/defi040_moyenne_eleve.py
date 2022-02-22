#Créez un programme qui lit deux notes d'un élève et calcule sa moyenne, en affichant un message à la fin, en fonction de la moyenne obtenue :
#Moyenne inférieure à 5,0 : ÉCHEC
#Moyenne entre 5,0 et 6,9 : RÉCUPÉRATION
#Moyenne 7.0 ou supérieure : APPROUVÉ
premier_note = float(input("Entrez la première note: "))
deuxieme_note = float(input("Entrez la deuxième note: "))
moyenne = (premier_note + deuxieme_note) / 2
print("Note 1 = {} note 2 = {}, la moyenne est {}".format(premier_note, deuxieme_note, moyenne))
if moyenne >= 7:
    print("APPROUVÉ, l'eleve a été approuvé")
elif moyenne < 7 and moyenne >= 5:
    print("RÉCUPÉRATION, l'evele est en recuperation")
else:
    print("ÉCHEC, il doit refaire l'année")

