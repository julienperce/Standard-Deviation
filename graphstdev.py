import main
import matplotlib.pyplot as plt
import numpy as np


dataSet = main.dataSet
average = main.average(main.dataSet)  
stDev = main.stdev  
calculated = [] # list that will get appended with (dataset[i] - stDev)
accepted = []
rejected = []

for i in range (0, len(dataSet)):
    calcMeanDev = float(dataSet[i] - stDev)
    calculated.append(calcMeanDev)
    print(calcMeanDev)

for i in range (0, len(calculated)):
    if calculated[i] >= (-3 * stDev) and calculated[i] <= (3 * stDev):
        accepted.append(calculated[i])
    else:
        rejected.append(calculated[i])

print(f'The rejected values were {rejected}')

for i in range (0, len(accepted)):
    1s = []
    2s = []
    3s = []
    if accepted[i] <= stdev:
        1s.append(accepted[i])
    elif accepted [i] >= stdev and accepted[i] <= (2 * stDev) and accepted[i] <= (-2 * stDev):
        2s.append(accepted[i])
    elif accepted [i] >= stdev and accepted[i] <= (3 * stDev) and accepted[i] <= (-3 * stDev):
        3s.append(accepted[i])

negXAxis = ((-3 * stDev)) # xMin
posXAxis = ((3 * stDev)) # xMax
negYAxis = (0) # yMin
posYAxis = (100) # yMax


plt.title("Standard Deviation graphed to a 99.99% accuracy")
plt.axis([negXAxis, posXAxis, negYAxis, posYAxis])
plt.xlabel("[-3σ;  3σ]")

print(f'The accepted values were {accepted}')
plt.hist(accepted)
plt.show()