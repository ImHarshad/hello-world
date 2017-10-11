from sklearn import tree
import sys
features = [[140,1], [130,1], [150,0], [170,0]]
labels = [0, 0, 1, 1]

while(True):
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(features, labels)
	x = input('Weight (in gms):')
	y = input('Texture (0-Bumpy & 1-Smooth):')
	z = [[int(x), int(y)]]
	i = clf.predict([ [x,y] ])
	found = 0

	if (i==0):
		print("The Fruit is an Apple!")
		for [a,b] in features:
			#print([a,b])
			if ([a,b] == [int(x), int(y)]):
				#print('Found')
				found = 1
				break
		if(found == 0):
			features = features + z
			labels = labels + [int(i)]
		
	else:
		print("The Fruit is an Orange!")
		for [a,b] in features:
			#print([a,b])
			if ([a,b] == [int(x), int(y)]):
				#print('Found')
				found = 1
				break
		if(found == 0):
			features = features + z
			labels = labels + [int(i)]

	print(features)
	print(labels)
	i = input('Do you want to Continue? 1-Yes & 0-No: ') 
	if(int(i)==0):
		sys.exit(0)
