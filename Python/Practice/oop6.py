
class Demo:
    A = 10                      #Class Variable
    def __init__(self):
        print("Inside Init (Construstor)")
        self.B = 20             #Instance Variable

    def fun_instance(self):     #instance Method
        print("inside instance Method")
        print(self.B)
        print(self.A)
        print(Demo.A)
        
    @classmethod
    def fun_class(cls):
        print("inside class Method")
        print(cls.A)
        print(Demo.A)
        
    @staticmethod
    def fun_static():
        print("inside Static Method")
        print(Demo.A)
    
    def __del__(self):
        print("Inside del (Disstructor)")

def main ():

    Demo.fun_static()
    

if __name__=="__main__":
    main()
