
def main():
#       batch = [Python,PPA,LSP,Angular]
#       fees=[12500,15000,21000,15500]

        fees = {"Python": 12500,"PPA":1500,"LSP":21000,"Angular":15500}
        print(fees)

        print("Please enter batch name : ")
        batch = input()

        print("Your enterd batch name is : ",batch)
        
        print("Fees is : ",fees[batch])

if __name__=="__main__":
    main();