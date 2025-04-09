# Develop a program that computes the power of a number N and prints the result.

n = int(input("Enter a number:"))

for i in range(n+1):
    power = n ** i
print("Power of number",n,":",power)

# another method
base = int(input("Enter base no:"))
exp = int(input("Enter exp no:"))
result = 1

while exp != 0:
    result = result * base
    exp = exp - 1
print("Power of number",base,":",result)
