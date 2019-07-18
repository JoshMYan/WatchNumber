# File name: app.py
# Created by Haodong Chen
# on June 14, 2019
# All rights reserved.

from run import support, experiment
import time

def main(logFile, t, rate, *hiddenNodes):
    mean = 0
    logFile.write(support.current())
    logFile.write("\nTrained for 3000 times and tested for 1000 times.")
    logFile.write("\nRepeat times: " + str(t))
    logFile.write("\n    In: 784; Out: 10; ")
    logFile.write("\n    Learning rate: " + str(rate))
    logFile.write(";\n    Hidden layers: " + str(hiddenNodes) + ";\nAccuracy: ")
    watch.reset()
    for i in range(t):
        experiment.refresh()
        accuracy = experiment.do(rate, *hiddenNodes)
        logFile.write(str(round(accuracy, 2)) + " ")
        mean += accuracy
    timeSpent = str(round(watch.lap(), 5))
    mean = 1.0 * mean / t
    logFile.write("\nMean accuracy: " + str(round(mean, 3)))
    logFile.write("\nAction takes " + timeSpent + " seconds.")
    logFile.write("\n\n")
    logFile.flush()
    print("Run", t, "times with learning rate of", rate, "given the hidden layers as", hiddenNodes, "completed in " + timeSpent + " seconds.")


f = open("./experiment.log", 'a')
watch = support.stopwatch()
# main(f, 20, 0.22, 100, 100)
# main(f, 20, 0.22, 200, 100)
# main(f, 20, 0.22, 200, 200)
main(f, 20, 0.22, 220)
main(f, 20, 0.22, 240)
main(f, 20, 0.22, 260)
main(f, 20, 0.22, 280)
f.close()
