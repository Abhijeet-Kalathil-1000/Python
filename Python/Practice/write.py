

def main():
    print("Enter file name you want to open : ")
    name = input()

    fd = open(name,"w")

    print("Enter the data that you want ot write in file. ")
    data = input()

    fd.write(data)
    fd.close()

if __name__=="__main__":
    main()