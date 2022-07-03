# Assignment 3_3 	Min number

def main():
    Data = []
    count=int(input("Enter numbr of elements : "))

    for i in range(count):
        Data.append(int(input()))
    print ("Entered list is : ",Data)
    print ("Maximum number is : ",min(Data))
    
if __name__=="__main__":
    main();