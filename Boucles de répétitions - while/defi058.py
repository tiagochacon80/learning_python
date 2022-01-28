#Jeu de devinettes

nombre_ordi = 5
tentatives = 1
print('Bonjour! Je suis ton ordinateur...Je viens de penser un numéro entre 0 e 10.')
print('Est-ce que tu serais capable de le deviner? ')
nombre_utilisateur = int(input("Informez un numéro entre 0 e 10: "))
while nombre_utilisateur != nombre_ordi:
    if nombre_utilisateur > nombre_ordi:
        nombre_utilisateur = int(input('Moins... Essayez à nouveau: '))
    else:
        nombre_utilisateur = int(input('Plus... Essayez a nouveau: '))
    tentatives = tentatives + 1
print("Vous avez reussi après", tentatives, "tentatives, le numéro est ", nombre_ordi, "Félicitation!")