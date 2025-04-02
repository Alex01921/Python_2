name = input("Enter your name:")
dob = int(input("Enter your year of birth:"))
age = 2025 - dob
print("Name of person:", name)
print("Year of birth:", dob)
print("Age of person:", age)
if( age >= 60):
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")
