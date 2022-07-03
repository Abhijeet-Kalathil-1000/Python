# Assignment 7_4
def DigitSum(a):
     
    if a < 10:
        return a
    else:
        return a % 10 + DigitSum(a//10)

def main ():
    value = int(input("Enter a number : "))
    
    ret = DigitSum(value)
    print("Sum of digits is: ",ret)


if __name__=="__main__":
    main()