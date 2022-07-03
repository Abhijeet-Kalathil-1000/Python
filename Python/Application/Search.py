# Assignment 3_4 	Search

def FreqSearch(value1,value2):
    count =0.0
    freq={}
    for i in value2:
        freq[value1] = value2.count(i)  
    return freq

def main():
    Data = []
    elements=int(input("Enter numbr of elements : "))

    for i in range(elements):
        Data.append(int(input()))
    print ("Entered list is : ",Data)
    
    temp=int(input("Enter the element you want to search : "))
    ret = FreqSearch(temp,Data)
    print("Frequesncy of ", temp," in the list is : ",ret)

if __name__=="__main__":
    main()