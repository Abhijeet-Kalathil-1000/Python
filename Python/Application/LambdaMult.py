# Assignment 4_2     Lamda Func muliply two num
def main ():

    mult = lambda a,b : a*b

    value1=int(input("enter the 1st number : "))
    value2=int(input("enter the 2nd number : "))

    ret = mult(value1,value2)

    print("Multiplication is : ",ret)

if __name__=="__main__":
    main()