#Un programme qui lit la vitesse d'une voiture et s'elle dépasse la vitesse 80km, affiche un message, disant qu'il doit payer une amende
vitesse = int(input("Quelle est la vitesse du véhicule? "))
if vitesse > 80:
    print("ATTENTION!! Vous avez dépassé la limite de vitesse permi qui est de 80km!!!")
    print("Vous devez payer une amande!")
else:
    print("Bonne journée, conduisez prudemment")