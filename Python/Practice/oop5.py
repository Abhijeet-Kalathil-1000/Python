
class Demo:
    A = 10                      #Class Variable
    def __init__(self):
        print("Inside Init (Construstor)")
        self.B = 20             #Instance Variable

    def fun_instance(self):     #instance Method
        print("inside instance Method")

    @classmethod
    def fun_class(cls):
        print("inside class Method")

    @staticmethod
    def fun_static():
        print("inside Static Method")
    
    def __del__(self):
        print("Inside del (Disstructor)")

def main ():
    
    Demo.fun_class()
    Demo.fun_static()
    
    obj = Demo()                   #Object Creation
    obj.fun_instance()
    #obj.fun_static()
    #obj.fun_class()

if __name__=="__main__":
    main()
    

"""
                    decoraotor  parameter    Call by
Instance Method         0         self      Obj. func name
Class Method            1         cls       class. func  name(obj also allword but not good prac)
Static Method           1          -        class. func  name(obj also allword but not good prac)

"""