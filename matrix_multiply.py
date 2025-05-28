l1 = [[1,2,3],[2,3,4],[3,4,5]]
l2 = [[1,2,1],[2,2,3],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(l1)):
    for j in range(len(l2[0])):
        for k in range(len(l2)):
            result[i][j] = result[i][j] + l1[i][k]*l2[k][j]
print("Multiplication of two matrices:")
print("\n")

for i in range(len(l1)):
    for j in range(len(l2)):
        print(result[i][j], end = ' ')
    print("\n")
