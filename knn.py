import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_mldata
from sklearn import neighbors


def loadData():
	mnist = fetch_mldata('MNIST original')
	return mnist

def dataProssess(data):
	x,y = data['data'],data['target']
	xtrain,xtest,ytrain,ytest = x[:60000],x[60000:],y[:60000],y[60000:]
	return xtrain,xtest,ytrain,ytest

def knn(xtrain,ytrain):
	clf = neighbors.KNeighborsClassifier(algorithm = 'ball_tree')
	clf.fit(xtrain,ytrain)
	return clf

def acess(clf,xtest,ytest):
	ypredict = clf.predict(xtest)
	score = accuracy_score(ypredict,ytest)
	print(score)

def save(clf):
	joblib.dump( './knn.py', clf )

def main():
	mnist = loadData()
	xtrain,xtest,ytrain,ytest = dataProssess(mnist)
	clf = knn(xtrain,ytrain)
	acess(clf,xtest,ytest)
	clf = knn(x,y)
	save(clf)

if __name__ == '__main__':
	main()

