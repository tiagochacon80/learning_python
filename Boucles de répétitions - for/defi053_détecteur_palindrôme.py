#
phrase = input("Entrez une phrase: ").strip().upper()#enelver les espaces, laisser tous les lettres majuscules
mots = phrase.split()#diviser par mots
ensemble = "".join(mots)#Mettre les mots ensemble
envers = ""
for lettre in range(len(ensemble) - 1, -1, -1):
    envers += ensemble[lettre]
print(ensemble, envers)
if envers == ensemble:
    print("Nous avons un palindrôme")
else:
    print("Nous n'avons pas un palindrôme")









