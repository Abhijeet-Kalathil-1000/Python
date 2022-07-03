
def add(a,b):
    ans= a+ b
    return ans

def main ():
    print("enter 1st number")
    no1=int(input())

    no2=int(input("enter 2nd number "))

    ret=add(no1,no2)

    print("answer is : ",ret)


if __name__=="__main__":
    main()