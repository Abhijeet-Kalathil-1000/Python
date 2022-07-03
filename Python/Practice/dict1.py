
def main():
        fees=[12500,15000,21000,15500]

        print(fees)

        print("Please enter batch name : ")
        batch = input()

        print("Your enterd batch name is : ",batch)
        if batch == "ppa" or "PPA":
            print("Fee is :",fees[1])
        elif batch == "python"  or "Python" :
            print("Fee is :",fees[0])
        elif batch == "lsp"  or "LSP" :
            print("Fee is :",fees[2])
        elif batch == "angular" or "Angular" :
            print("Fee is :",fees[3])
        else:
            print("Wrong Entry")

if __name__=="__main__":
    main();