#Programme qui approuve un prêt bancaire pour acheter une maison.
#Le montant du prêt ne peut pas depasser 30% de son revenu annuel.
montant_maison = int(input("Quel est le montant de la maison: "))
salaire = float(input("Informez le salaire anuelle du acheteur: "))
annees = int(input("Combien d'années remboursez-vous le prêt: "))

porcentage_salaire = (salaire / 12) * 0.3
versement_mensuel = (montant_maison / annees) / 12
if versement_mensuel > porcentage_salaire:
    print("Pour payer une maison de {}$ en {} années le versement sera de {:.2f}".format(montant_maison, annees, versement_mensuel))
    print("Le prêt a été refusé, cela depasse 30% de votre salaire")
else:
    print("Pour payer une maison de {}$ en {} années le versement sera de {:.2f}".format(montant_maison, annees, versement_mensuel))
    print("Le prêt est approuvé")
