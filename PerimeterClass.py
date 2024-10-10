#Create a class called Perimeter
#this file should contain all the functions
#to calculate Area
import math
class Perimeter:

    #Create a constructor that initializes all variables in the class 
    def __init__(self,p,c,t,s,r,l,w,b,h):
        self.periRect = p
        self.circumF = c
        self.periTri = t
        self.sides = s
        self.radius = r
        self.length = l
        self. width = w
        self.base = b
        self.height = h
    
    def PerimeterOfRectangle(self):
        #length = int(input("Enter length:\n"))
        #width = int(input("Enter width:\n"))
        Perimeter = self.length+self.length+self.width+self.width
        print("Perimeter Of Rectangle is:", Perimeter,"cm squared")

    def CircumferenceOfCircle(self):
        #Radius = int(input("Enter the radius:\n"))
        Perimeter = math.pi*self.radius *self.radius
        print("CircumferenceOfCircle is:", Perimeter ," cm square")

    
    def PerimeterOfTriangle(self):
        #s= int(input("Enter sides:\n"))
        Perimeter= self.sides + self.sides + self.sides + self.sides
        print("Perimeter Of Triangle is:",Perimeter,"cm squared")      
