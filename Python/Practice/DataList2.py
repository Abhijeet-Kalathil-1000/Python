
# List
# Sequestial
# Indexed
# Data and List both are Mutable
# Allows duplicate
# List is Hetrogenious (takes diffrent data types )


Data = [11,21,51,101,3.14]
print("Data type is : ",type(Data))
print("Length is : ",len(Data))
print("Actuall Data type is : ",Data)


print("Data from 0th index:",Data[0])
print("Data from 3rd index:",Data[3])

Data[0] = 12

print("New Data from 0th index:",Data[0])

Data.append(111)
print(Data)


Data.insert(2,51)
print(Data)

print(Data[-1])
print(Data[-2])