
import array as ARR

def main():
    print("Array demo")
    data =ARR.array('i',[10,20,30,40])

    print(data)
    print("Length of array ",len(data))
    print("Type of array ",type(data))


    for i in range(len(data)):
        print(data[i])

    print("---------------------")
    for no in data:
        print(no,end="\t")

if __name__=="__main__":
    main();