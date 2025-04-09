# Develop a program that computes the factorial of a number N and prints the result.
n = int(input("Enter a number:"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial of number",n,":",fact)
