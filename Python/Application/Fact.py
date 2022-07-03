# Assignment 7_5
def Fact(a):
    if a > 1:
        return (a * Fact(a -1))
    else :
        return a

def main ():
    value= int(input("Enter a number to check its factorial : "))
    ret = Fact(value)
    print("Factorial of %d is %d" %(value,ret))

if __name__=="__main__":
    main()