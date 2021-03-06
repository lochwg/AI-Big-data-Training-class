from sklearn.datasets import load_iris
from sklearn import tree
# =============================================================================
# from sklearn.cross_validation import train_test_split
# =============================================================================
from sklearn.model_selection import train_test_split

iris = load_iris()
iris_x = iris.data
iris_y = iris.target

train_X, test_X, train_y, test_y = \
train_test_split(iris_x, iris_y, test_size = 0.3)

clf = tree.DecisionTreeClassifier()
iris_clf = clf.fit(train_X, train_y)

test_y_predicted = iris_clf.predict(test_X)
print(test_y)
