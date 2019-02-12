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
I trained the ADALINE unit for 3000 epochs using a learn rate = 0.0001, and reduced the error given by the SSE function to a mean of 0.5, and a rate of success of 0.8 in average. 
The learning rate and the number of epochs can be modified in order to get a better performance.

