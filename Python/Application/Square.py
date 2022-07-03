# Assignment 4_1     Lamda Func power 2

def main ():

    fact = lambda a : 2**a

    no1 = int(input("Enter the number to check power of 2 : "))
    ret = fact(no1)
    print("Ans is ",ret)


if __name__=="__main__":
    main()