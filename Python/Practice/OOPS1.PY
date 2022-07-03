#Encapsulation = Class = Charceteristics + Behaviour

# Class Defination
class Arithematic:
    def __init__(self,a,b):        #Constructor
        print("inside init(Cons) ")
        self.no1=a      #Characteristic
        self.no2=b         #Characteristic

    def Add(self):      #Behaviour
        ans = self.no1 + self.no2
        return ans

def main ():

    x=int(input(("Enter 1st number : ")))
    
    y=int(input(("Enter 2nd number : ")))

    
    obj = Arithematic(x,y)   # object creation 
    ret = obj.Add()          #Call funtion via object

    print("Answer is : ",ret)

if __name__=="__main__":
    main()