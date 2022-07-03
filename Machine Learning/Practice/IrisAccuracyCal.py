from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def AccuracyDecisionTree(data_train, data_test, target_train, target_test):

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)
    Accuracy = accuracy_score(target_test,predictions)

    return Accuracy

def AccuracyKNeighbor(data_train, data_test, target_train, target_test):

    classifier = KNeighborsClassifier()
    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)
    Accuracy = accuracy_score(target_test,predictions)

    return Accuracy

def main():
    iris = load_iris()

    data = iris.data
    target = iris.target
    #spliting in main so that both fucnt get same set of splited data sets
    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5)
    
    Accuracy = AccuracyDecisionTree(data_train, data_test, target_train, target_test)
    print("Acuracy with descion tree is ",Accuracy*100,"%")
    
    Accuracy = AccuracyKNeighbor(data_train, data_test, target_train, target_test)
    print("Acuracy with descion tree is ",Accuracy*100,"%")
    
if __name__ == "__main__":
    main()