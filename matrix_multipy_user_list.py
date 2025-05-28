l1=[]
l2=[]
result=[]

m1=int(input("Enter the order m1:")) 
n1=int(input("Enter the order n1:"))
m2=int(input("Enter the order m2:")) 
n2=int(input("Enter the order n2:"))

if n1 == m2:
   print("Valid")
else:
    print("Invalid")
    
print("Enter elements for l1:")
for i in range(m1):
    row = []
    for j in range(n1):
        x=int(input())
        row.append(x)
    l1.append(row)
print("Enter elements for l2:")
for i in range(m2):
    row = []
    for j in range(n2):
        y=int(input())
        row.append(y)
    l2.append(row)    
print("L1:",l1)
print("L2:",l2)

for i in range(len(l1)):
    row = []
    for j in range(len(l2[0])):
        for k in range(len(l2)):
            result[i][j] = result[i][j] + l1[i][k]*l2[k][j]
