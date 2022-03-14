from random import choice

#case = creer_carte(5, 5, 8)
#print(case)
#voisins_potentiels = [(case.coordonnees[0] + i, case.coordonnees[1] + j) for i, j in

                                  #[(0, -1), (-1, 0), (1, 0), (0, 1)]]
listT = [1, "tarte", 3, 4][0:2]
print(listT)

data = {"name": "Wayne", "age": 45}
print(data["name"])



stats = {'key1':20, 'key2':20, 'key3': 44}
max_key = max(stats, key = stats.get)
min_key = min(stats, key = stats.get)
print(min_key)