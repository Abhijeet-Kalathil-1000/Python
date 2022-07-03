import os

def main():
    print("Enter file name you want to delete : ")
    name = input()

    if os.path.exists(name):
        os.remove(name)
        print("File deleted ")

    else:
        print("No such file ")

if __name__=="__main__":
    main()