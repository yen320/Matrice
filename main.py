
matriceC = []

# choix de l'oppération 
print("")
print(" 1.Addition   2.Multiplication par une matrice   3.Transposée   4.Déterminant   5.Multiplication par un scalaire")
print("")
opération = input("> ")

if opération == "1" :
    print("Attention aux régles des matrices !")
    print("l'oppération est A+B")

        # taille de la matrice 
    nxma = input("taille de la matrice A ( nm , entre 1 et 9) : ")
    nxma.split(" ")
    print(nxma)
    na = nxma[0]
    ma = nxma[1]
    print("{} lignes".format(na))
    print("{} colones".format(ma))

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
    
    x=0
    for i in range(na):
        print(matriceA[x])
        x+=1
    
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

    x=0
    for i in range(nb):
        print(matriceB[x])
        x+=1

    # verification que les dimmentions sont les memes 
    if na != nb or ma != mb :
        print("régles des matrices non réspécté")
        print("")
        print("")
        quit
    # je comprend pas bien ce que je fais j'essay de faire l'addition
    y = 0
    for i in range(len(matriceA)):
        ligne_addition = [x + y for x, y in zip(matriceA[y], matriceB[y])]
        matriceC.append(ligne_addition)
        y += 1
    # afficher la matrice des 2 magnères 
    print("C ={}".format(matriceC))
    x = 0
    for i in range(na):    
        print(matriceC[x])
        x+=1


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

    x=0
    for i in range(na):
        print(matriceA[x])
        x+=1

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

    x = 0
    for i in range(na):
        print(matriceA[x])
        x += 1

    # création d'une matrice "vide" de la taille de T
    matriceT = []
    nt = int(ma)
    mt = int(na)

    for i in range(nt):
        ligne = [0] * mt
        matriceT.append(ligne)

    # début de la transposé 

    x = 0
    for i in range(nt):
        y = 0
        for i in range(mt):
            matriceT[x][y] = matriceA[y][x]

            y +=1
        x +=1

    # afficher la matrice des 2 magnères 
    print(matriceT)
    x = 0
    for i in range(na):    
        print(matriceC[x])
        x+=1

elif opération == "4":
    print("4")

elif opération == "5":
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

    na = int(na)
    ma = int(ma)

    x = 0
    for i in range(na):
        print(matriceA[x])
        x += 1

    # multiplicateur
    k = int(input("multiplicateur : "))

    # création d'une matrice "vide" de la taille de A
    matriceC = []

    for i in range(na):
        ligne = [0] * ma
        matriceC.append(ligne)

    # début de la transposé 

    x = 0
    for i in range(na):
        y = 0
        for i in range(ma):
            matriceC[x][y] = k * matriceA[x][y]

            y +=1
        x +=1

    # afficher la matrice des 2 magnères 
    print(matriceA)
    x = 0
    for i in range(na):    
        print(matriceC[x])
        x+=1

elif opération == "4":
    print("4")


else :
    print("wrong number")



print("")
print("")
