while True:
    dejeune = input("Avez-vous dejeuné ce matin? (o/n) ")
    alimentation = float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes? "))
    activite_physique = int(input("Combien de minutes d'activité physique avez-vous effectué? "))

    ajouter_un_jour = input('Voulez vous ajouter un jour ? ( o/n)')
    ajouter_un_jour == 'n'
    if (alimentation < 0.2 or alimentation > 0.8):
        print('Vous ne mangez pas équilibré tous les jours! Visez 50% de fruits et légumes.')


