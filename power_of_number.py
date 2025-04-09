# Develop a program that computes the power of a number N and prints the result.

n = int(input("Enter a number:"))

for i in range(n+1):
    power = n ** i
print("Power of number",n,":",power)
