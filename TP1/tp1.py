#Travail pratique 1 pour le cours d'introduction à la programmation avec Python
print("Bienvenue au calculaeur (calculateur santé/sans T)")

dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
alimentation = float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes? "))
activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))


if alimentation < 0.2 or alimentation > 0.8:
    print('Vous ne mangez pas équilibré tous les jours! Visez 50% de fruits et légumes.')
if activite_physique < 30:
    print('Vous ne faites pas suffisament de sport! Visez 30 minutes par jour en moyenne.')
if dejeune == 'n':
    print('Attention! Vous ne devez pas faire du sport sur un estomac vide!')