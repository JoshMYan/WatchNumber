# File name: app.py
# Created by Haodong Chen
# on June 14, 2019
# All rights reserved.

import numpy
import neurons

# create network
recognizer = neurons.NeuronsNetwork(0.1, 784, 10, 100)

# training
trainSet = open('./dataset/mnist_debug', 'r')
for l in trainSet:
    data = numpy.asarray(l.split(','), 'int')
    target = numpy.zeros(10) + 0.1
    target[data[0]] = 0.99
    recognizer.train((numpy.asfarray(data[1:]) / 255.0 * 0.99 + 0.01), target)
trainSet.close()

# testing
testSet = open('./dataset/mnist_debug_test', 'r')
for l in testSet:
    data = numpy.asarray(l.split(','), 'int')
    result = recognizer.query(numpy.asfarray(data[1:]) / 255.0 * 0.99 + 0.01).tolist()
    first = second = third = 0
    for i in range(len(result)):
        p = result[i][0]
        if p > result[third][0]:
            third = i
            if p > result[second][0]:
                third = second
                second = i
                if p > result[first][0]:
                    third = second
                    second = first
                    first = i
    print(data[0], 'Most Possible:', first, 'of', result[first][0] * 100, '%\n')
