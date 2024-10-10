#AreaOfRectangleFunction.py
#Function to get area of rectangle
import math
#Defining the function
def AreaOfRectangle():
    length = int(input("Enter length:\n"))
    width = int (input("Enter width"))
   area = length*width
print("Area Of Rectangle is: ", area , "cm squared")

#outside of function5
#here, we Call the function
#AreaOfRectangle()

#AreaOfCircle


def AreaOfCircle():
    #Pie=int(3.14)
    Radius = int(input("Enter the radius of the circle:\n"))
    area = math.pi *Radius *Radius
    print("AreaOfCircle is:", area ," cm square")

 
 
 
 
AreaOfCircle()

            