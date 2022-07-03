class Demo:
    def __init__(self):
        self.A=10
        self.__B=20    #private valieable (add 2 _ in start )


    def fun(self):
        print("Inside fun")
        self.__gun()

    def __gun(self):
        print("inside Gun")

def main():
    obj = Demo()
    
    obj.fun()
    #obj.__gun()

if __name__=="__main__":
    main()