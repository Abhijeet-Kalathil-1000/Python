# Assignment 3_2 	Max number

def main():
    Data = []
    count=int(input("Enter numbr of elements : "))

    for i in range(count):
        Data.append(int(input()))
    print ("Entered list is : ",Data)
    print ("Maximum number is : ",max(Data))
    
if __name__=="__main__":
    main();