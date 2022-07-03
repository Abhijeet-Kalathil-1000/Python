
def sub(a,b):
    ans = 0
    ans = a-b
    return ans

def SmartSub(func_name):
    def Inner(a,b):
        if a < b:
            a,b = b,a
        return func_name(a,b)

    return Inner

sub = SmartSub(sub)

def main ():
    No1 = int(input("Enter 1st number : "))
    No2 = int(input("Enter 2nd number : "))

    ret = sub(No1,No2)
    print("Sub is : ",ret)


if __name__=="__main__":
    main()