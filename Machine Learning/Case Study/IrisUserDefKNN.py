from sklearn import tree
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class MyKNN():
    def fit(self,TrainingData,TrainingTarget):
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget

    def predict(self,TestData):
        predictions =[]
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    
    def closest(self,row):
        bestdistance = euc(row,self.TrainingData[0])
        bestindex = 0
        for i in range(1,len(self.TrainingData)):
            dist = euc(row,self.TrainingData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i
        return self.TrainingTarget[bestindex]

def MyKNeighbor(data_train, data_test, target_train, target_test):
    iris = load_iris()
    data = iris.data
    target = iris.target
    
    border="-"*50
    print(border)
    print("Actual DataSet")
    print(border)

    for i in range(len(iris.target)):
        print("ID : %d,Label %s, Feature :%s"%(i,iris.data[i],iris.target[i]))
    print("Size of Actual Data set %d"%(i+1))

    print(border)
    print("Training data set")
    print(border)
    for i in range(len(data_train)):
        print("ID : %d,Label %s, Feature :%s"%(i,data_train[i],target_train[i]))
    print("Size of Training Data set %d"%(i+1))

    print(border)
    print("Test data set")
    print(border)
    for i in range(len(data_train)):
        print("ID : %d,Label %s, Feature :%s"%(i,data_test[i],target_test[i]))
    print("Size of Test Data set %d"%(i+1))
    print(border)

    classifier = MyKNN()
    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)
    Accuracy = accuracy_score(target_test,predictions)
    

    return Accuracy

def main ():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5)

    Accuracy = MyKNeighbor(data_train, data_test, target_train, target_test)
    print("Accuracy is ",Accuracy*100,"%")
    
    # this formatter will label the colorbar with the correct target names
    formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

    plt.figure(figsize=(5, 4))
    plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
    plt.colorbar(ticks=[0, 1, 2], format=formatter)
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.show()

if __name__=="__main__":
    main()