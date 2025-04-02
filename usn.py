usn = input("Enter your USN:")
name = input("Enter your name:")

phy = int(input("Enter your physics marks:"))
chem = int(input("Enter your chemistry marks:"))
py = int(input("Enter your phython marks:"))

total = phy + chem + py
percentage = (total / 300) * 100

print("USN:", usn)
print("Name:", name)
print("Total marks:", total)
print("Percentage:", percentage, "%")

if(phy >= 40 and chem >= 40 and py >= 40):
    print("3 subject pass")
elif((phy >= 40 and chem >= 40) or (phy >= 40 and py >= 40) or (chem >= 40 and py >= 40)):
    print("2 subject pass")
elif(phy >= 40 or chem >= 40 or py >= 40):
    print("1 subject pass")
else:
    print("All subject fail")
