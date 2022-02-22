#Démarrez un programme qui lit l'année de naissance d'un jeune
#et l'informe, selon son âge, s'il va encore s'enrôler dans l'armée, si c'est l'heure exacte de s'enrôler
#ou si l'heure de l'enrôlement est dépassée. Votre programme doit également afficher le temps restant ou en retard.

import datetime
annee_actuelle = datetime.datetime.now()
date = annee_actuelle.date() #Date actuelle
annee = int(date.strftime("%Y")) #extraction de l'année actuelle
annee_naissance = int(input("Entrez votre l'année de naissance: "))
sexe = input("Entrez votre sexe: [M] masculin [F] féminin: ").upper()
if sexe == "F":
    print("Vous n'avez pas besoin de faire l'enrolement militaire.")
else:
    age_actuelle = annee - annee_naissance
    print("La personne qui est né en {} a {} ans en {}".format(annee_naissance, age_actuelle, annee))
    if age_actuelle > 18:
        annee_retard = age_actuelle - 18
        print("Vous est {} an(s) en retard pour le enrolement militaire".format(annee_retard))
        print("Votre enrolement militaire a été en {}".format(annee_naissance + 18))
    elif age_actuelle < 18:
        mineur = 18 - age_actuelle
        print("Il manque {} ans pour l'enrolement militaire".format(mineur))
        print("Votre enrolement militaire sera en {}".format(annee + mineur))
    else:
        print("Vous devez faire votre inscriptions pour l'enrolement militaire cette année")


