#Create a class called Area
# This class will contain all the 
#--functions to calculate Area
import math
class Area:

    #create a constructor
    #This is a function also referred to 
    # as_init
    def __init__(self,l,w,r,b,h):
        self.length = l
        self.width = w
        self.radius = r
        self.base = b
        self.height = h

    def AreaOfRectangle(self):
        length = int(input("Enter length:\n"))
        width = int (input("Enter width"))
        area = self.length* self.width
        print("Area Of Rectangle is: ", area , "cm squared")



    def AreaOfCircle(self):
        Pie=int(3.14)
        Radius_1 = int(input("Enter the radius:\n"))
        area = math.pi*self.radius *self.radius
        print("AreaOfCircle is:", area ," cm square")

        #end of functiom
    
#Create OBJECTS here outside of the class
#RObj = Area()
#CObj = Area()

   


#Test Questions

    


    def AreaOfTriangle(self):
        b= int(input("Enter base:\n"))
        h= int(input("Enter height:\n"))
        Area= self.base*self.height
        print("Area Of Triangle is:",Area,"cm squared")



