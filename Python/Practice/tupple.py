
#Tupple

#Hetrogenious
#Indexed
#Sequential
#Ordered
#Allows Duplicate 
#Data of tupple is Immutable

data=(10,20,30,40,"Abhijeet",10)

print("Data type is : ",type(data))
print("Elements are : ",data)
print("Element at 0th index",data[0])
print("Element at 0th index",data[3])
print("Last data",data[-1])

#data[0]=11  #Data intupple are immutable 

data.append(20)

print("New data : ",data)