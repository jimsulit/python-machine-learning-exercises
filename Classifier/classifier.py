# import submodule tree of scikit-learn that will help us build ML model decision tree
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
# Var X refers a list of list containing the three metrics that we will use
# Var Y contains a list of gender labels relating to X
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Stores our decision tree classifier
clf = tree.DecisionTreeClassifier()
# call fit method on the classifier variable which takes two arguments - X & Y; result is stored on updated clf var
clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

#Prints gender prediction
print(prediction)
