matriceA =[[1,2,3],[4,5,6],[7,8,9]]
matriceB =[[9,2,1],[3,8,7],[0,1,4]]
matriceC =[[0,0,0],[0,0,0],[0,0,0]]

nc = 3
mc = 3

n = 0
m = 0
for i in range(3):
    x = 0
    for i in range(3):
        print(matriceA[n][x], matriceB[x][m])
        matriceC[n][m] += matriceA[n][x] * matriceB[x][m]
        x += 1
    m += 1
    print("")

print(matriceC)
