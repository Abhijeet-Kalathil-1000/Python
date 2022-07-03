from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import pandas as pd

def WinePredictor(x_train,x_test,y_train,y_test):

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)
    predictions = model.predict(x_test)

    print("Accuracy : ",accuracy_score(y_test,predictions)*100,"%\n")
        
def CheckAccuracy(data,x,y):

    print("_"*50)
    print("\nAccuracy Calculator \nAlgoritm : K Nearest Neighbour")

    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.5)

    for i in range(4,30):
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(x_train,y_train)
        predictions = model.predict(x_test)       
        print("For N = ",i," Accuracy : ",accuracy_score(y_test,predictions)*100,"%")

def main():
    data = pd.read_csv('WinePredictor.csv')
    print(data.head())
 
    x = data.drop('Class',axis=1)
    y = data["Class"]

    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

    print("_"*50)
    print("\nCaseStudy : Wine Preedictor \nAlgoritm : K Nearest Neighbour")

    WinePredictor(x_train,x_test,y_train,y_test)
    CheckAccuracy(data,x,y)
    
if __name__ == "__main__":
    main()