from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

def PlayPredictor():

    data = pd.read_csv('PlayPredictor.csv')
    print(data.head())
    
    label_encoder= preprocessing.LabelEncoder()
    data['Wether'] = label_encoder.fit_transform(data["Wether"])
    data['Temperature'] = label_encoder.fit_transform(data["Temperature"])

    print(data.head())
 
    x = data.drop('Play',axis=1)
    y = data["Play"]

    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.5)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(x_train,y_train)
    
    predictions = model.predict(x_test)

    cm= confusion_matrix(y_test,predictions)
    print("confurion Matrix : \n",cm)
    print("Accuracy : ",accuracy_score(y_test,predictions)*100,"%")
        
    plt.scatter(y_test,predictions)
    plt.xlabel('True values')
    plt.ylabel('Predicitions')
    plt.show()


def main():
    print("_"*50)
    print("CaseStudy : Play Preedictor \n Algoritm : K Nearest Neighbour")

    PlayPredictor()
    
if __name__ == "__main__":
    main()