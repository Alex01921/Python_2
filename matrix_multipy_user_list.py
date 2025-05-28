l1 = []
l2 = []
result = []

m = int(input("Enter the order m:"))
n = int(input("Enter the order n:"))
p = int(input("Enter the order p:"))
q = int(input("Enter the order q:"))

if (m < 1 or n < 1 or p < 1 or q < 1):
    print("Error:Kindly enter valid order ")
    exit()

if n == p:
    print("Valid matrix")
else:
    print("Invalid matrix")
    exit()

print("Matrix of order:", m, "*", q, "will be obtained.")

print("Enter elements for l1:")
for i in range(m):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    l1.append(row)

print("Enter elements for l2:")
for i in range(p):
    row = []
    for j in range(q):
        y = int(input())
        row.append(y)
    l2.append(row)

print("L1:", l1)
print("L2:", l2)

for i in range(m):
    row = []
    for j in range(q):
        sum1 = 0
        for k in range(p):
            sum1 += l1[i][k] * l2[k][j]
        row.append(sum1)
    result.append(row)

print("Multiplication of two matrices:")
print(result)
