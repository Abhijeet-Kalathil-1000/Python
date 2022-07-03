def Div(A,B):
    ans = 0.0
    try:
        ans = A / B
    except ZeroDivisionError :
        print("Exception Occured")
    return ans

def main():
    no1 = int(input("Enter 1st num : "))
    no2 = int(input("Enter 2nd num : "))

    ret = Div(no1,no2)
    print("Div is : ",ret)

if __name__=="__main__":
    main()