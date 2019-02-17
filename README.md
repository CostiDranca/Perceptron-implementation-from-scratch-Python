# Perceptron-implementation-from-scratch-Python
This repository contains two implementations for the Perceptron/ADALINE unit,  one with α -LMS rule for ADALINE unit, and the other uses the delta rule. For a better understanding of the perceptron, writing the algorithms is a big help.

The data set used for training and testing is the iris data set, both of them are capable to clasify the first two classes of iris flowers.
These implementations are from scratch coded in Python using only numpy. Both of them use:
- Gradient Descent for the update of weights and bias.
- The mean squared error (MSE)
- Criterion function is sum of squared error (SSE)

Files:
1.ADALINE_LMS:

ADALINE unite is formed only by the weights and bias, the ouput is y=x'w+b, where y is the output, x is the input, w is the weights and b is the bias, it doesn't have an activation function, but for better practice, the function getOutput is used for the propagation of input through unit. From 100 flowers, 90 of them are used for training and the others 10 are used for testing. 
I trained the ADALINE unit for 3000 epochs using a learning rate = 0.0001, and reduced the error given by the SSE function to a mean of 0.5, and a rate of success of 0.8 in average. 
The learning rate and the number of epochs can be modified in order to get a better performance.

2.Delta Rule Perceptron
This file contains an implementation for the a perceptron with logsig activation function, and for updateing of weights uses the delta rule (based on partial derivative of the error function with respect to each weight). The learning rule looks like: Wk= Wk-1 + r * (d - y)*y(1-y)*x, where Wk is the values of weights at epoch k, y is the output of perceptron and x is the input. From 100 flowers, 80 of them are used for training and the others 20 are used for testing. 
I trained the perceptron for 3000 epochs using a learning rate = 0.001, and reduced the error given by the SSE function to a mean 0f 0.1, and a rate of success of 100% in average.
The learning rate and the number of epochs can be modified in order to get a better performance.

A problem of these implementations is that the samples of training and testing aren't selected randomly, this could lead to an overfitting for the training of the perceptron, for better results the training data shoul be selected randomly. Another problem is that the data quantity is very low.
