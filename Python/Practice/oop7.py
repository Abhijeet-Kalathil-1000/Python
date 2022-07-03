class Demo:
    def __init__(self):
        self.A=10
        self.__B=20    #private valieable (add 2 _ in start )


    def fun(self):
        print("Inside fun")
        print(self.A)
        print(self.__B)

def main():
    obj = Demo()
    print(obj.A)
    obj.fun()
        
if __name__=="__main__":
    main()