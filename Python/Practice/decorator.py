
def Division(A,B):
    Ans = 0.0
    Ans = A/B
    return Ans


def main ():
    No1 = int(input("Enter 1st number : "))
    No2 = int(input("Enter 2nd number : "))

    ret = Division (No1,No2)
    print("Div is : ",ret)

if __name__=="__main__":
    main()