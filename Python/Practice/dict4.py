
def main():

    data={"Even":[2,4,6,8],"Odd":[1,3,5,7,9], "Other":[32.,42.3]}

    print(data["Even"][0]);
    for key in data:
        print("\n",key)
        for i in data[key]:
            print(i,end=" ")
            
if __name__=="__main__":
    main();