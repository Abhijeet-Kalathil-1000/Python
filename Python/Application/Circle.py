# Assignment 5_2          Circle 

class Circle:

    PI = 3.14

    def __init__(self):

        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    def Accept(self):
        self.radius = float(input("Enter Radius : "))

    def CaculateArea(self):
        self.area = Circle.PI*(self.radius**2)

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI*self.radius

    def Display(self):
        print("Radius is : ",self.radius)
        print("Area is : ",self.area)
        print("Circumference is : ",self.circumference)

def main ():
    print("Main")
    Obj1 = Circle()

    Obj1.Accept()
    Obj1.CaculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()

    Obj2.Accept()
    Obj2.CaculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__=="__main__":
    main()