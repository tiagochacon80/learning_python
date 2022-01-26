print("Bienvenue au calculaeur (calculateur santé/sans T)")
jour = 0
ajouter_un_jour = 'o'
liste_de_jours = []
somme = 0
while ajouter_un_jour != 'n':
    jour = jour + 1
    print('\nJour {}'.format(jour))
    dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
    alimentation = float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes? "))
    activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))
    liste_de_jours.append([dejeune, alimentation, activite_physique])
    somme = somme + activite_physique
    ajouter_un_jour = input("Voulez-vous ajouter un jour? (o/n) ")
#moyenne = somme / jour #Duvida p/ professor
#print(liste_de_jours)
print()
entre_dans_if = [False] * 3
print("Calcul des conseils en cours...")
for i in range(len(liste_de_jours)):
    if (liste_de_jours[i][1] < 0.2 or liste_de_jours[i][1] > 0.8) and entre_dans_if[0] == False:
        print("Vous ne mangez pas équilibré tous les jours! Visez 50% de fruits et légumes.")
        entre_dans_if[0] = True
    if liste_de_jours[i][2] < 30 and entre_dans_if[1] == False:
    #if  moyenne < 30 and entre_dans_if[1] == False: #Duvida p/ professor
        print('Vous ne faites pas suffisamment de sport! Visez 30 minutes par jour en moyenne. ')
        entre_dans_if[1] = True
    if (dejeune == "n" and activite_physique >= 30) and entre_dans_if[2] == False:
        print("Attention! Vous ne devez pas faire du sport sur un estomac vide! ")
        entre_dans_if[2] = True
    if  entre_dans_if[0] == True and entre_dans_if[1] == True and entre_dans_if[2]:
        i = len(liste_de_jours) + 1
print('Fin du calcul!')
print()
print('Passez une belle journée!')
