#Jeu de devinettes

nombre_ordi = 5
tentatives = 1
nombre_utilisateur = int(input("Informez un numéro entre 0 e 10: "))
while nombre_utilisateur != nombre_ordi:
    nombre_utilisateur = int(input("Ton numéro n'est pas correct, essayer à nouveau: "))
    tentatives = tentatives + 1
print("Vous avez reussi après", tentatives, "tentatives, le numéro est ", nombre_ordi, "Félicitation!")