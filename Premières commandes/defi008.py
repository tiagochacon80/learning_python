#Faire un programme que lit un nombre en mètres et calcule en centimètres et millimètres.
metres = int(input('Entrez la quantité de mètres: '))
centimetres = metres * 100
millimetres = metres * 1000
print('Mètres = {:.2f}, centimètres = {:.2f} cm, millimètres = {:.2f} mm'.format(metres, centimetres, millimetres))
