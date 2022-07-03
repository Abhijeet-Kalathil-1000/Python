
import array as ARR

def main():
    print("Array demo")
    data =ARR.array('d',[10,20.54,30.22,40.4])

    print(data)
    print("Length of array ",len(data))
    print("Type of array ",type(data))


    for i in range(len(data)):
        print(data[i])

    print("---------------------")
    for no in data:
        print(no,end="\t")
    
    print("\nTypecode ",data.typecode)

if __name__=="__main__":
    main();