import os

def main():
    print("Enter file name you want to open : ")
    name = input()

    if os.path.exists(name):
        fd = open(name,"r")
        data = fd.read()

        print("Data from the file is :",data)
        fd.close()

    else:
        print("No such file ")

if __name__=="__main__":
    main()