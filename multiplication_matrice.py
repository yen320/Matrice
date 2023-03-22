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

