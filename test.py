# File name: test.py
# Created by Haodong Chen
# on June 15, 2019
# All rights reserved.

import random

def test1():
    print('hhhhh')
    pass

def test2():
    count = 0
    mnist = open('./dataset/mnist_test.csv', 'r')
    debug = open('./dataset/mnist_debug_test', 'w')
    while count < 50:
        line = mnist.readline()
        if random.random() < 0.1:
            debug.write(line)
            count += 1
    mnist.close()
    debug.flush()
    debug.close()
    pass

def test3():
    pass

test1()
# test2()
# test3()
