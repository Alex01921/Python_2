# Develop a program that computes the factorial of a number N and prints the result.
n = int(input("Enter a number:"))
fact = 1
i = 1
while(i<=n):
    fact = fact * i
    i += 1
print("Factorial of number",n,":",fact)
