
def main():
    data = {10,20,30,40}
    mylist = [10,20,30,40]
    print("Type :",type(data))
    print("Lenght :",len(data))
    print("Data from set :",data)
    print("Data from list :",mylist)
    
    #   print(data[0])

    print("Data travlersal")
    for no in data:
        print(no,end=" ")
    data1= {10,20,30,40,60.3}
    print("\nData from set :",data1)


if __name__=="__main__":
    main()