na = 2
ma = 2
nb = 2
mb = 2

nc = na
mc = mb 

matriceA = [[0,2], [3,4]]
matriceB = [[3,2], [4,4]]
matriceC = []

# verification :

if na != mb or ma != nb :
    print("opération impossible")
    quit()

for i in range(nc):
    ligne = [0] * mc 
    matriceC.append(ligne)

print(matriceC)

