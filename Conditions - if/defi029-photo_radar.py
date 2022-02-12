#Un programme qui lit la vitesse d'une voiture et s'elle dépasse la vitesse 80km, affiche un message, disant qu'il doit payer une amende
vitesse = float(input("Quelle est la vitesse du véhicule? "))
amende = 0
if vitesse > 80:
    print("ATTENTION!! Vous avez dépassé la limite de vitesse permi qui est de 80km!!!")
    amende = round((vitesse - 80) * 7)
    print(f"Vous devez payer une amende de {amende}$!")
else:
    print("Bonne journée, conduisez prudemment")