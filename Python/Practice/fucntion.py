def add(no1,no2):
    ans =0
    ans = no1 + no2
    return ans

def main():
    print("Enter first no")
    value1=int(input())

    print("Enter Second no")
    value2=int(input())

    ret = add(value1,value2)
    print("Add is ",ret)

if __name__==("__main__"):
    main()