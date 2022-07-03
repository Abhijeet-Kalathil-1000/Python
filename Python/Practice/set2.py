
def main ():
    print("enter number of elements : ")
    size = int(input())

    data={0}

    for i in range(size):
        print("Enter element no : ",i+1)
        no = int(input())
        data.add(no)
    print("Data",data)

    print("Entere data search")
    value = int(input())

    if value in data:
        print("Yes")
    else:
        print("No")


if __name__=="__main__":
    main()