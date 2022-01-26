#Travail pratique 1 pour le cours d'introduction à la programmation avec Python
print("Bienvenue au calculaeur (calculateur santé/sans T)")
jour = 0
ajouter_un_jour = 'o'
somme = 0
while ajouter_un_jour != 'n':
    jour = jour + 1
    print('\nJour {}'.format(jour))
    dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
    alimentation = float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes? "))
    activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))
    somme = somme + activite_physique
    ajouter_un_jour = input("Voulez-vous ajouter un jour? (o/n) ")