# Develop a program that prints the first N numbers of Fibonacci sequence.
n = int(input("Enter a nth term:"))
n1 = 0
n2 = 1

print("Fibonacci series:", n1,n2, end = " ")

for i in range (2, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end =" ")
