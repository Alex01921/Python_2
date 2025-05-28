l1=[]
l2=[]
result=[]

m1=int(input("Enter the order m1:")) 
n1=int(input("Enter the order n1:")) 

print("Enter elements for l1:")
for i in range(m1):
    row = []
    for j in range(n1):
        x=int(input())
        row.append(x)
    l1.append(row)
print("Enter elements for l2:")
for i in range(m1):
    row = []
    for j in range(n1):
        y=int(input())
        row.append(y)
    l2.append(row)    
print("L1:",l1)
print("L2:",l2)

result = [[0 for _ in range(n1)] for _ in range(m1)]

for i in range(m1):
    for j in range(n1):
        result[i][j]=l1[i][j]+l2[i][j]
        
print("Addition of two matrices:")
print("\n")
for i in range(m1):
    for j in range(n1):
        print(result[i][j],end = ' ')
    print('\n')
