from sklearn.datasets import load_iris

iris = load_iris()

print("Feature name of irirs data set")
print(iris.feature_names)

print("Target name of irirs data set")
print(iris.target_names)

print("First 10 elements from iris data set")

for i in range(len(iris.target)):
    print("ID: %d,Label: %s,Feature : %s"%(i,iris.data[i],iris.target[i]))
