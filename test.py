    # taille de la matrice 
nxma = input("taille de la matrice A ( nm , entre 1 et 9) : ")
nxma.split(" ")
print(nxma)
na = nxma[0]
ma = nxma[1]
print(na)
print(ma)

    # deffinition de la matrice
matriceA = []
x = 1
for i in range(int(na)):
    ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x)).split(",")
    print(ligne)
    matriceA.append(ligne)
    x += 1
print("A = {}".format(matriceA))
    # Matrice "A" créé

print(matriceA[0])
