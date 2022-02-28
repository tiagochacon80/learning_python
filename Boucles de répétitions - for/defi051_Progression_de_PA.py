print("="*30)
print("     10 thermes d'un PA    ")
print("="*30)
premier = 0 #int(input("Premier therme: "))
raison = 2 #int(input("Raison: "))
#Version 1
for i in range(0, 10):
    print(f"{premier + raison * i}", end='- ')

print()
#Version 2
dixieme = premier + (10 - 1) * raison
for i in range(premier, dixieme + raison, raison):
    print(f"{i}", end="- ")
print("Fin")
