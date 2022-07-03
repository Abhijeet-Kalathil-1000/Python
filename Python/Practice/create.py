

def main():
    print("Enter file name you want to create : ")
    name = input()

    fd = open(name,"x")

    print("File gets created with the infomarion  as : ",fd)

if __name__=="__main__":
    main()