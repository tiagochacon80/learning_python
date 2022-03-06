#fonction avec listes
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valeur = [6, 3, 9, 2, 0, 5]
dobra(valeur)
print(valeur)
