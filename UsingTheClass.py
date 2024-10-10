#as a user
from Classes import Area
print=int("what is your choice?")
l = int(input("Enter length:\n"))
w = int(input("Enter width:\n"))
r = int(input("Enter radius:\n"))
b = int(input("Enter base:\n"))
h = int(input("Enter height:\n"))
#Create objects and assign values
RObj=Area(l,w,0)

#Use objest to access the AreaOfRectangle function
RObj.AreaOfRectangle()

CObj=Area(0,0,r)
CObj.AreaOfCircle()

BObj=Area(b,h,0)
BObj.AreaOfTriangle()

TriArea=int input("Enter the base and height:\n")
if r>=2 and TriArea<=3:
    print("AreaOfTriangle")

elif 






