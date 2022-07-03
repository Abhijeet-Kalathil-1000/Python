def fun():
    print("Inside Fun")

def gun(func_name):
    print("Inside gun")
    func_name()

def main ():
    gun(fun)

if __name__=="__main__":
    main()