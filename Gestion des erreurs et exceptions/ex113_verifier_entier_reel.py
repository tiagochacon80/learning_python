def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERREUR: Entrez un nombre entier valide.\033[m')
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mL'utilisateur a entre un autre numero.\033[m")
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERREUR: entrez un nombre reel valide.")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mL'utilisateur a entrez un autre numero.\033[m")
            return 0
        else:
            return numero

numero1 = leiaInt("Entrez un entier:")
numero2 = leiaFloat("Entrez un réel:")
print(f"Le nombre saisi entier était: {numero1} et réel était {numero2}")
