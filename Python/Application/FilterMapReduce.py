# Assignment 4_3     Filter,Map & Reduce 
from functools import reduce

def myFilter(x):                #Filter values between 70 & 90 
    if x <=90 and x>=70:
        return True
    else:
        return False

def myMap(a):           #Map elemnts by adding 10
    return a + 10

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

    mapped=map(myMap,Data2)   
    Data3 = list(mapped)                  #map
    print("Mapped list is : ",Data3)

    reduced = reduce((lambda x, y: x * y),Data3)
    print("Product of the list is : ",reduced)

if __name__=="__main__":
    main()