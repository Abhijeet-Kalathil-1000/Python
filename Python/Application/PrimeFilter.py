# Assignment 4_5     Filter,Map & Reduce 
from functools import reduce

def myFilter(value):
    count=0
    if (value > 1):
        for i in range(2,value):
            if(value % i) == 0:                 #Prime filter
                count = count + 1
        if count > 1:
            return False
        else:
            return True
    
def main ():
    Data = []
    Data2 =[]
    Data3 =[]
    element=int(input("Enter the number of elements you want in the list : "))
    for i in range(element):
        Data.append(int(input()))
    print("Your list is : ",Data)


    filtered = filter(myFilter,Data)
    for i in filtered:                      #filter
        Data2.append(i)
    print("Filtered list is : ",Data2)

    mapped=map(lambda a: a*2,Data2)   
    Data3 = list(mapped)                  #map
    print("Mapped list is : ",Data3)

    reduced = reduce(max,Data3)        #reduce
    print("Product of the list is : ",reduced)

if __name__=="__main__":
    main()