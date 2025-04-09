# Develop a program that inputs names of five students and displays if your name is present in the five names.
your_name = "Ashok"
a = input("Enter your name:")
b = input("Enter your name:")
c = input("Enter your name:")
d = input("Enter your name:")
e = input("Enter your name:")

if(a==your_name or b == your_name  or c == your_name or d == your_name or e == your_name ):
    print("Name is present", your_name)
else:
    print("Your name is not present.")
