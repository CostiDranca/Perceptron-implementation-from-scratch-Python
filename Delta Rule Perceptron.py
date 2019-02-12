import numpy as np
import random
import sys
import pandas as pd
from sklearn.datasets import load_iris

def purelin(weights,bias,X):
    resultat=0.0
    for i in range(len(X)):
        resultat+=weights[i]*X[i]
    resultat+=bias
    return resultat

def logsig(weights, bias,X):
    resultat=0.0
    for i in range(0,len(weights)):
        resultat+=weights[i]*X[i]
    resultat+=bias
    return 1.0/(1.0+np.exp(-resultat))

iris = load_iris()
dataInput = np.array([iris.data[0]])
labels=np.array(iris.target[0])


dataTest=np.array(iris.data[10])
for i in range(1,len(iris.data) - 50):
    if (i % 5) != 0:
        dataInput=np.vstack([dataInput,np.array(iris.data[i])])
        labels=np.append(labels,iris.target[i])
    else:
        dataTest=np.vstack([dataTest,np.array(iris.data[i])])

weights=[random.random(),random.random(),random.random(),random.random()]
bias=random.random()
rataLearn=0.001

epoca=0
eroare=0.0
nrEpoc=3000

while epoca<=nrEpoc:
    eroare=0.0
    epoca+=1
    for i in range (len(dataInput)):
        resultat=logsig(weights,bias,dataInput[i])
        #print"Rezultatul: ", resultat
        eroare+=((labels[i]-resultat)**2)/2.0
        for j in range(len(weights)):
            weights[j]+=rataLearn*(labels[i]-resultat)*resultat*(1-resultat)*dataInput[i][j]
        bias += rataLearn * (labels[i]-resultat)*resultat*(1-resultat)
    if epoca%100 == 0:
        print "Epoca: ",epoca,": ",eroare
print weights
print bias

reusite=0.0
for i in range (len(dataTest)):
    prezicere=logsig(weights,bias,dataTest[i])
    if(prezicere<0.5):
        print "0",iris.target[i*5]
        if (iris.target[i*5] == 0):
            reusite = reusite +1
    else:
        print "1",iris.target[i*5]
        if (iris.target[i*5] == 1):
            reusite = reusite +1
print "Success Rate: ",reusite/(len(dataTest))