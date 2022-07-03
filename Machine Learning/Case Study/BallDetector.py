from sklearn import tree

def myML(weight,surface):
    BallsFeatures =[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(BallsFeatures,Names)

    result = clf.predict([[weight,surface]])

    if result == 1:
        print("it looks like Tennis Ball")
    elif result == 2:
        print("it looks like cricket Ball")

def main():
    print("-------------ML-----------")

    weight=input("Enter weight ")
    surface=input("How is the surface smooth or rough ")

    if surface.lower() =="rough":
        surface = 1
    elif surface.lower() =="smooth":
        surface = 0
    else:
        print("Enter valid input")
        exit()

    myML(weight,surface)

if __name__=="__main__":
    main()