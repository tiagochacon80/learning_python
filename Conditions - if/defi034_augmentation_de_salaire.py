salaire = float(input("Entre votre salaire: "))
augmentation = 0
if salaire <= 1250:
    augmentation = salaire * 1.15
    print("La personne qui gagne {}$, va gagner {:.2f}$".format(salaire, augmentation))
else:
    augmentation = salaire * 1.10
    print("La personne qui gagne {}$, va gagner {:.2f}$".format(salaire, augmentation))