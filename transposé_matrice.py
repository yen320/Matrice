na = 2
ma = 2

nt = ma
mt = na

matriceA = [[0,2], [3,4]]
matriceT = []

# création d'une matrice "vide" de la taille de T
for i in range(nt):
    ligne = [0] * mt
    matriceT.append(ligne)

x = 0
for i in range(nt):
    y = 0
    for i in range(mt):
        matriceT[x][y] = matriceA[y][x]

        y +=1
    x +=1

print(matriceT)
