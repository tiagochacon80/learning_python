#Faire un programme que lit trois notes d'un étudiant et calcule sa moyenne.
note1 = float(input("Entrez la premiere note: "))
note2 = float(input("Entrez la deuxième note: "))
note3 = float(input("Entrez la troisième note: "))
moyenne = (note1 + note2 + note3)/3
print('La moyenne est {:.2f}'.format(moyenne))