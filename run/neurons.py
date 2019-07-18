# File name: neurons.py
# Created by Haodong Chen
# on June 14, 2018
# All rights reserved.

import numpy
import scipy.special as scsp

class NeuronsNetwork:

    def __init__(self, rate, inputNodes, outputNodes, *hiddenNodes):
        self.rate = rate
        self.inputNodes = inputNodes
        self.outputNodes = outputNodes
        self.hiddenNodes = hiddenNodes
        self.wih = numpy.random.normal(0.0, pow(self.hiddenNodes[0], -0.5), (self.hiddenNodes[0], self.inputNodes))
        self.multi = len(self.hiddenNodes) > 1
        if self.multi:
            self.whh = []
            for i in range(1, len(self.hiddenNodes)):
                self.whh.append(numpy.random.normal(0.0, pow(self.hiddenNodes[i], -0.5), (self.hiddenNodes[i], self.hiddenNodes[i - 1])))
        self.who = numpy.random.normal(0.0, pow(self.outputNodes, -0.5), (self.outputNodes, self.hiddenNodes[-1]))
        pass

    def train(self, i, t):
        inputArr = numpy.array(i, ndmin=2).T
        targetArr = numpy.array(t, ndmin=2).T
        start = scsp.expit(numpy.dot(self.wih, inputArr))
        m = [start,]
        if self.multi:
            for i in range(len(self.whh)):
                m.append(scsp.expit(numpy.dot(self.whh[i], m[i])))
        o = scsp.expit(numpy.dot(self.who, m[-1]))
        oe = targetArr - o
        hoe = numpy.dot(self.who.T, oe)
        self.who += self.rate * numpy.dot((oe * o * (1.0 - o)), numpy.transpose(m[-1]))
        hhe = [hoe,]
        if self.multi:
            for i in range(1, len(m)):
                hhe.append(numpy.dot(self.whh[len(self.whh) - i].T, hhe[i - 1]))
                self.whh[len(self.whh) - i] += self.rate * numpy.dot((hhe[i - 1] * m[len(m) - 1] * (1.0 - m[len(m) - 1])), numpy.transpose(m[len(self.whh) - i]))
        self.wih += self.rate * numpy.dot((hhe[-1] * m[0] * (1.0 - m[0])), numpy.transpose(inputArr))
        pass

    def query(self, l):
        # weights
        inputArr = numpy.array(l, ndmin=2).T
        start = scsp.expit(numpy.dot(self.wih, inputArr))
        middle = start
        if self.multi:
            for i in self.whh:
                middle = scsp.expit(numpy.dot(i, middle))
        final = scsp.expit(numpy.dot(self.who, middle))
        return final

    def save(self):
        pass
