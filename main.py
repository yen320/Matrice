

matriceC = []

# choix de l'oppération 
print("")
print(" 1.Addition   2.Multiplication   3.Transposée   4.Déterminant")
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
    print("lignes : {}".format(na))
    print("colones : {}".format(ma))

        # deffinition de la matrice
    matriceA = []
    x = 1
    for i in range(int(na)):
        ligne = []
        print("ligne {}".format(x))
        y = 1
        for j in range(int(ma)):
            ligne.append(int(input("colone {} ".format(y))))
            y += 1
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé
    
    print(matriceA[0])
    print(matriceA[1])

        # taille de la matrice 
    nxmb = input("taille de la matrice B ( nm , entre 1 et 9) : ")
    nxmb.split(" ")
    print(nxmb)
    nb = nxmb[0]
    mb = nxmb[1]
    print("lignes : {}".format(nb))
    print("colones : {}".format(mb))

        # deffinition de la matrice
    matriceB = []
    x = 1
    for i in range(int(nb)):
        ligne = []
        print("ligne {}".format(x))
        y = 1
        for j in range(int(mb)):
            ligne.append(int(input("colone {} ".format(y))))
            y += 1
        matriceB.append(ligne)
        x += 1
    print("B = {}".format(matriceB))
        # Matrice "B" créé

    print(matriceB[0])
    print(matriceB[1])

    # verification que les dimmentions sont les memes 
    if na != nb or ma != mb :
        print("régles des matrices non réspécté")
        quit
    # je comprend pas bien ce que je fais j'essay de faire l'addition
    y = 0
    for i in range(len(matriceA)):
        ligne_addition = [x + y for x, y in zip(matriceA[y], matriceB[y])]
        matriceC.append(ligne_addition)
        y += 1
    print("C ={}".format(matriceC))
    print(matriceC[0])
    print(matriceC[1])


elif opération == "2" :
    print("Attention aux régles des matrices !")
    print("l'oppération est AxB")

        # taille de la matrice 
    nxma = input("taille de la matrice A ( nm , entre 1 et 9) : ")
    nxma.split(" ")
    print(nxma)
    na = nxma[0]
    ma = nxma[1]
    print("lignes : {}".format(na))
    print("colones : {}".format(ma))

        # deffinition de la matrice
    matriceA = []
    x = 1
    for i in range(int(na)):
        ligne = []
        print("ligne {}".format(x))
        y = 1
        for j in range(int(ma)):
            ligne.append(int(input("colone {} ".format(y))))
            y += 1
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé

    print(matriceA[0])
    print(matriceA[1])

        # taille de la matrice 
    nxmb = input("taille de la matrice B ( nm , entre 1 et 9) : ")
    nxmb.split(" ")
    print(nxmb)
    nb = nxmb[0]
    mb = nxmb[1]
    print("lignes : {}".format(nb))
    print("colones : {}".format(mb))

        # deffinition de la matrice
    matriceB = []
    x = 1
    for i in range(int(nb)):
        ligne = []
        print("ligne {}".format(x))
        y = 1
        for j in range(int(mb)):
            ligne.append(int(input("colone {} ".format(y))))
            y += 1
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
    print("lignes : {}".format(na))
    print("colones : {}".format(ma))

        # deffinition de la matrice
    matriceA = []
    x = 1
    for i in range(int(na)):
        ligne = []
        print("ligne {}".format(x))
        y = 1
        for j in range(int(ma)):
            ligne.append(int(input("colone {} ".format(y))))
            y += 1
        matriceA.append(ligne)
        x += 1
    print("A = {}".format(matriceA))
        # Matrice "A" créé

    print(matriceA[0])
    print(matriceA[1])

elif opération == "4":
    print("4")

else :
    print("wrong number")



print("")
print("")
