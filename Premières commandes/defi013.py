#Faire un programme qui lit le salaire de l'employé et affiche son nouveau salaire avec une augmentation de 15%

salaire = float(input('Informez votre salaire actuel: '))
nouveau_salaire = salaire * 1.15
print('Votre nouveau salaire est de {:.2f}$'.format(nouveau_salaire))
