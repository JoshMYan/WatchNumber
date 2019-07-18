# File name: experiment.py
# Created by Haodong Chen
# on June 18, 2019
# All rights reserved.

import numpy
from run import neurons
from dataset import handler


def refresh(trainT = 3000, testT = 1000):
    # generate files
    handler.update("mnist_train.csv", "mnist_debug", trainT if trainT <= 60000 else 60000, 55000.0 / trainT if trainT < 55000 else 1)
    handler.update("mnist_test.csv", "mnist_debug_test", testT if testT <= 10000 else 10000, 9000.0 / trainT if trainT < 9000 else 1)


def do(rate, *hiddenNodes):

    # create network
    recognizer = neurons.NeuronsNetwork(rate, 784, 10, *hiddenNodes)

    # training
    trainSet = open('./dataset/mnist_debug', 'r')
    trainCount = 0
    for l in trainSet:
        trainCount += 1
        data = numpy.asarray(l.split(','), 'int')
        target = numpy.zeros(10) + 0.1
        target[data[0]] = 0.99
        recognizer.train((numpy.asfarray(data[1:]) / 255.0 * 0.99 + 0.01), target)
    trainSet.close()

    # testing
    testSet = open('./dataset/mnist_debug_test', 'r')
    report = []
    testCount = 0
    correctFirst = correctSecond = correctThird = incorrect = 0
    for l in testSet:
        testCount += 1
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
        if data[0] == first:
            correctFirst += 1
        elif data[0] == second:
            correctSecond += 1
        elif data[0] == third:
            correctThird += 1
        else:
            incorrect += 1
        report.append((data[0], first, result[first][0], second, result[second][0], third, result[third][0]))
    testSet.close()

    # output report
    # support.report(recognizer, trainCount, testCount, correctFirst, correctSecond, correctThird, incorrect, True)

    return 1.0 * correctFirst / testCount

