
matriceA = [[0,2], [3,4]]
matriceB = [[3,2], [4,4]]
matriceC = []

x = 0
for i in range(len(matriceA)):
    ligne_addition = [x + y for x, y in zip(matriceA[x], matriceB[x])]
    matriceC.append(ligne_addition)
    x += 1

print(matriceC)

# marche pas 

