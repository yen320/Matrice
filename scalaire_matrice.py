na = 2
ma = 2

k = 4

matriceA = [[0,2], [3,4]]
matriceB = []

# création d'une matrice "vide" de la taille de T
for i in range(na):
    ligne = [0] * ma
    matriceB.append(ligne)

x = 0
for i in range(na):
    y = 0
    for i in range(ma):
        matriceB[x][y] = k * matriceA[x][y]

        y +=1
    x +=1

print(matriceB)
