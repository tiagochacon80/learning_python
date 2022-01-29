#Programme qui converti le real (R$) en USD (u$)
montant = float(input('Entrez un montant: '))
us = montant / 5.20
print('R$ {}, ça coute U$ {:.2f}'.format(montant, us))