#IF STATEMENT
Age=int(input("what is your age?\n"))
if Age>=12 and Age <=27:
    print("You are Gen Z")


elif Age>=28 and Age<=43:
    print("You are a Millennials")


elif Age>=44 and Age<=59:
    print("You are Gen X")


elif Age>=60 and Age<=78:
    print("You are a Bommer")

else:
    print("Sorry!You are out of bounds...")
