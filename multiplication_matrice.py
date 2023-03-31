na = 2
ma = 2
nb = 2
mb = 2

nc = na
mc = mb 

matriceA = [[0,2], [3,4]]
matriceB = [[3,2], [4,4]]
matriceC = []

# verification de la taille des matrices 
if na != mb or ma != nb :
    print("opération impossible")
    quit()

# création d'une matrice "vide" de la taille de C
for i in range(nc):
    ligne = [0] * mc 
    matriceC.append(ligne)

# calcules écrit à la main d'une matrice 2x2 (pas ouf) => à automatiser
matriceC[0][0] = matriceA[0][0] * matriceB[0][0] + matriceA[0][1] * matriceB[1][0]
matriceC[0][1] = matriceA[0][0] * matriceB[0][1] + matriceA[0][1] * matriceB[1][1]
matriceC[1][0] = matriceA[1][0] * matriceB[0][0] + matriceA[1][1] * matriceB[1][0]
matriceC[1][1] = matriceA[1][0] * matriceB[0][1] + matriceA[1][1] * matriceB[1][1]

print(matriceC)

exit()

# calcule d'une matrice 3x3 idem
matriceC[n][m] = matriceA[n][x] * matriceB[y][m] + matriceA[n][x] * matriceB[y][m]

# création d'une matrice "vide" de la taille de A et B 
for i in range(na):
    ligne = [0] * ma
    matriceC.append(ligne)

x = 0
for i in range(na):
    y = 0
    for i in range(ma):
        matriceC[x][y] = matriceA[x][y] * matriceB[x][y]

        y +=1
    x +=1

print(matriceC)



# calcule matrice nxm (peut être avec matrice carré -> surement plus simple) 
x = 0
for i in range(nc):
    y = 0
    for i in range(mc):
        matriceC[x][y] = 

        y +=1
    x +=1