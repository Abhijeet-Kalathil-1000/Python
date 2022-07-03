
def main():

    data={"A":10,"B":20,"C":30,"D":40,"E":40,"F":55.4}

    print("Data : ",data)
    print("Type : ",type(data))
    print("Length : ",len(data))

    print(data["A"]);
    for key in data:
        print(" ",key,data[key],end="")

if __name__=="__main__":
    main();