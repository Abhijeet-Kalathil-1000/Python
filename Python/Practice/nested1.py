def outer():
    print("Inside Outer Fun")

    def inner():
        print("Inside inner Fun")

    return inner

def main ():
    func_name = outer()     #Its call to outter fun 
    func_name()             #Its call to inner fun 

if __name__=="__main__":
    main()