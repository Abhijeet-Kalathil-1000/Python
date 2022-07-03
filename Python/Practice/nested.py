
def outer():
    print("Inside Outer Fun")

    def inner():
        print("Inside inner Fun")

    inner()

def main ():
    outer()


if __name__=="__main__":
    main()