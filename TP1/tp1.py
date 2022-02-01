#Travail pratique 1 pour le cours d'introduction à la programmation avec Python
print("Bienvenue au calculaeur (calculateur santé/sans T)")

question_dejeune = ()
question_alimentation = ()
question_activite_physique = ()

jour = 0
ajouter_un_jour = True

while ajouter_un_jour:
    jour = jour + 1
    print('\njour {}.'.format(jour))
    dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
    alimentation = float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes? "))
    activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))

    question_dejeune = question_dejeune + (dejeune,)
    question_alimentation = question_alimentation + (alimentation,)
    question_activite_physique = question_activite_physique + (activite_physique,)

    question = input('Voulez vous ajouter un jour ? ( o/n)')
    ajouter_un_jour = question == 'o'

somme = 0
for activite_physique in question_activite_physique:
    somme = somme + activite_physique
nombre_elements = len(question_activite_physique)
moyenne = somme / nombre_elements
if moyenne < 30:
    print('Vous ne faites pas suffisamment de sport! Visez 30 minutes par jour en moyenne.')
if dejeune == 'n' and activite_physique >= 30:
    print('Attention! Vous ne devez pas faire du sport sur un estomac vide!')
if alimentation < 0.2 or alimentation > 0.8:
    alimentation_inadequate = True

if alimentation_inadequate:
    print('Vous ne mangez pas équilibré tous les jours! Visez 50% de fruits et légumes.')
print('Fin du calcul!')
print()
print('Passez une belle journée!')

