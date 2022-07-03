
def main():
    print("Enter file name you want to open : ")
    name = input()

    fd = open(name,"rb")

    print("Current Offset is : ",fd.tell())

    data = fd.read(2)

    print("Data is : ",data)
    print("Current Offset is : ",fd.tell())

    fd.seek(3,1)
    
    print("Current Offset is : ",fd.tell())

    data = fd.read()
    print(data)

if __name__=="__main__":
    main()


#0 means start
#1 means current 
#2 means end 