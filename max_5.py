a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
e = int(input("Enter fifth number:"))

if(a>b and a>c and a>d and a>e):
    print("Max = a",a)
elif(b>a and b>c and b>d and b>e):
    print("Max = b",b)
elif(c>a and c>b and c>d and c>e):
    print("Max = c",c)
elif(d>a and d>b and d>c and d>e):
    print("Max = d",d)
else:
    print("Max = e",e)
