#Programme qui demande une distance d'un voyage en km et calcule le prix du billet d'avion, les couts sont 0.50$/km jusqu'à 200km et 0.45$ pour les voyages plus long
distance = float(input("Entrez la distance de votre voyage: "))
prix = 0
if distance <= 200:
    prix = distance * 0.50
    print("Le prix de billet coûtera {:.2f}$".format(prix))
else:
    prix = distance * 0.45
    print("Le prix de billet coûtera {:.2f}$".format(prix))