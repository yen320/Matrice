

matriceC = []

# choix de l'oppération 
print("")
print(" 1.Addition   2.Multiplication   3.Transposée")
print("")
opération = input(">")

if opération == "1" :
    print("Attention aux régles des matrices !")
    print("l'oppération est A+B")

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
        ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x))
        ligne.split(",")
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé
    
        # taille de la matrice 
    nxmb = input("taille de la matrice B ( nm , entre 1 et 9) : ")
    nxmb.split(" ")
    print(nxmb)
    nb = nxmb[0]
    mb = nxmb[1]
    print(nb)
    print(mb)

        # deffinition de la matrice
    matriceB = []
    x = 1
    for i in range(int(nb)):
        ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x))
        ligne.split(",")
        matriceB.append(ligne)
        x += 1
    print("B = {}".format(matriceB))
        # Matrice "B" créé

    # verification que les dimmentions sont les memes 
    if na != nb or ma != mb :
        print("régles des matrices non réspécté")
        quit
    # je comprend pas bien ce que je fais j'essay de faire l'addition
    y = 0
    for i in range(matriceA):
        ligne_addition = [x + y for x, y in zip(matriceA[y], matriceB[y])]
        matriceC.append(ligne_addition)
        y += 1



elif opération == "2" :
    print("Attention aux régles des matrices !")
    print("l'oppération est AxB")

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
        ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x))
        ligne.split(",")
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé


        # taille de la matrice 
    nxmb = input("taille de la matrice B ( nm , entre 1 et 9) : ")
    nxmb.split(" ")
    print(nxmb)
    nb = nxmb[0]
    mb = nxmb[1]
    print(nb)
    print(mb)

        # deffinition de la matrice
    matriceB = []
    x = 1
    for i in range(int(nb)):
        ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x))
        ligne.split(",")
        matriceB.append(ligne)
        x += 1
    print("B = {}".format(matriceB))
        # Matrice "B" créé

elif opération == "3" :
    print("3")
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
        ligne = input("ligne {} : (1,2,3,4,5, ... )".format(x))
        ligne.split(",")
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé

else :
    print("wrong number")



print("")
print("")
