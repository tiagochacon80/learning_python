# Travail pratique 1 pour le cours d'introduction à la programmation avec Python
print("Bienvenue au calculaeur (calculateur santé/sans T)")

question_activite_physique = []

jour = 1
ajouter_un_jour = True
dejeune = 'n'
activite_physique = 0
ventre_vide = False
alimentation_inadequate = False

while ajouter_un_jour:

    print('\njour {}.'.format(jour))
    dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
    if dejeune == 'n':
        ventre_vide = True
    alimentation = float(input('Quelle fraction de votre alimentation a consisté de fruits et légumes? '))
    if alimentation < 0.2 or alimentation > 0.8:
        alimentation_inadequate = True
    activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))

    question_activite_physique.append(activite_physique)

    question = input('Voulez vous ajouter un jour ? (o/n) ')
    ajouter_un_jour = question == 'o'
    jour = jour + 1

somme = 0
for activite_physique in question_activite_physique:
    somme = somme + activite_physique

nombre_elements = len(question_activite_physique)
moyenne = somme / nombre_elements

if moyenne < 30:
    print('Vous ne faites pas suffisamment de sport! Visez 30 minutes par jour en moyenne.')
if ventre_vide and activite_physique >= 30:
    print('Attention! Vous ne devez pas faire du sport sur un estomac vide!')
if alimentation_inadequate:
    print('Vous ne mangez pas équilibré tous les jours! Visez 50% de fruits et légumes.')

print('Fin du calcul!')
print()
print('Passez une belle journée!')
