from sklearn import tree
features = [[140,1], [130,1], [150,0], [170,0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
i = clf.predict([ [160,0] ])
if (i==0):
	print("The Fruit is an Apple!")
else:
	print("The Fruit is an Orange!")
