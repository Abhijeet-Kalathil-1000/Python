class Demo:
    def __init__(self):
        self.i = 10
        self.j = 20

    def Add(self,a):
        print("Inside add with 1 para")

    def Add(self,a,b):
        print("Inside add with 2 para")

def main ():
        Obj = Demo()
        #Obj.Add(11)
        Obj.Add(11,10)

if __name__=="__main__":
    main()