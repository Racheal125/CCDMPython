#As a user
from PerimeterClass import Perimeter
choice=int(input("Enter 1,2,3 to calculate the following:\n1 for Perimeter\n2 for Circumference\n3 for Triangle\n"))

#if statement
if choice ==1:
    l=int(input("Enter length:\n"))
    w=int(input("Enter width:\n"))
    RObj= Perimeter(0,0,0,0,0,l,w,0,0)
    RObj.PerimeterOfRectangle()

elif choice ==2:
    r=int(input("Enter radius:\n"))
    CObj= Perimeter(0,0,0,0,r,0,0,0,0)
    CObj.CircumferenceOfCircle()

elif choice ==3:
    s=int(input("Enter sides:\n"))
    BObj=Perimeter(0,0,0,s,0,0,0,0,0)
    BObj.PerimeterOfTriangle()

else:
    print("Invalid choice")