import numpy as np
import random
import sys
import pandas as pd
from sklearn.datasets import load_iris

def getOutput(weights,bias,X):
    resultat=0.0
    for i in range(len(X)):
        resultat+=weights[i]*X[i]
    resultat+=bias
    return resultat



iris = load_iris()
print iris.target
dataInput = np.array([iris.data[0]])
labels=np.array(iris.target[0])

dataTest=np.array(iris.data[10])
for i in range(1,len(iris.data) - 50):
    if (i % 10) != 0:
        dataInput=np.vstack([dataInput,np.array(iris.data[i])])
        labels=np.append(labels,iris.target[i])
    else:
        dataTest=np.vstack([dataTest,np.array(iris.data[i])])
print labels
weights=[random.random(),random.random(),random.random(),random.random()]
bias=random.random()
rataLearn=0.0001
eroare=9999999.0
epoca=0
numberEp=3000
while epoca<=numberEp:
    epoca+=1
    resultat=np.array([0.0,0.0,0.0,0.0])
    eroareAct=0.0
    eroare=0.0
    for i in range(len(dataInput)):
        resultatulActual=getOutput(weights,bias,dataInput[i])
        eroareAct+=((labels[i]-resultatulActual))
        eroare+=(((labels[i]-resultatulActual))**2)/2
        for j in range(len(weights)):
            resultat[j]+=(labels[i]-resultatulActual)*(dataInput[i][j])
    weights+=rataLearn*resultat
    bias+=rataLearn*eroareAct
    if epoca%100 ==0:
        print eroare
    #print "Update: ",weights,bias,"\n"

print weights
print bias
print epoca

reusite = 0.0;
for i in range(len(dataTest)):
    result=getOutput(weights,bias,dataTest[i])
    if result <0:
        print "0",iris.target[i*10]
        if (iris.target[i*10] == 0):
            reusite = reusite +1
    else:
        print "1",iris.target[i*10]
        if (iris.target[i*10] == 1):
            reusite = reusite +1
print "Success Rate of perceptron is: ",(reusite/len(dataTest))*100,"%"
