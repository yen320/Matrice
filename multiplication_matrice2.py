# donées
matriceA =[[9,2],[3,8],[0,1]]
matriceB =[[1,2,3],[4,5,6]]

na = 3
ma = 2
nb = 2
mb = 3
nc = na
mc = mb

# création d'une matrice "vide" de la taille de C
matriceC = []

for i in range(na):
    ligne = [0] * mc
    matriceC.append(ligne)

print(matriceC)

# verif
if na != mb or ma != nb :
    print("! dimentions non compatibles !")
    quit()

# début du calcule
n = 0 
for i in range(na):
    m = 0
    for i in range(na):
        x = 0
        for i in range(ma):
            print(matriceA[n][x], matriceB[x][m])
            matriceC[n][m] += matriceA[n][x] * matriceB[x][m]
            x += 1
        m += 1
        print("")
    n += 1
    print("-")
    print("")

print(matriceC)
