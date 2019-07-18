# File name: app.py
# Created by Haodong Chen
# on June 14, 2019
# All rights reserved.

import time

def report(obj, trainCount, testCount, correctFirst, correctSecond = -1, correctThird = -1, incorrect = -1, isPercent = False):
    log = current() + "\nRecognizer:"
    log += "\n    Learning rate: " + str(obj.rate)
    log += "\n    Input node #:  " + str(obj.inputNodes)
    log += "\n    Hidden layers: " + str(obj.hiddenNodes)
    log += "\n    Output node #: " + str(obj.outputNodes)
    log += "\nTrained for " + str(trainCount) + " images, tested for " + str(testCount) + " images.\n"
    log += "Among tested data,\n    " + \
          (str(100.0 * correctFirst / testCount) + " %" if isPercent else str(correctFirst) + " out of " + str(testCount)) + " are correct.\n"
    if correctSecond >= 0:
        log += "    " + (str(100.0 * correctSecond / testCount) + " %" if isPercent else str(correctFirst) + " out of " + str(testCount)) + " are in the second choice.\n"
        if correctThird >= 0:
            log += "    " + (str(100.0 * correctSecond / testCount) + " %" if isPercent else str(correctFirst) + " out of " + str(testCount)) + " are in the third choice.\n"
    if incorrect >= 0:
        log += "    " + (str(100.0 * incorrect / testCount) + " %" if isPercent else str(incorrect) + " out of " + str(testCount)) + " are not included above.\n"
    log += "\n"
    print(log)
    f = open("./test.log", 'a')
    f.write(log)
    f.flush()
    f.close()

def current():
    return time.strftime("%b. %d, %Y %a. %H:%M:%S", time.localtime())
