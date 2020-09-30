import main
import matplotlib.pyplot as plt
import numpy as np


dataSet = main.dataSet
average = main.average(main.dataSet)  
stDev = main.stdev  
calculated = [] # list that will get appended with (dataset[i] - stDev)

for i in range (0, len(dataSet)):
    calcMeanDev = float(dataSet[i] - stDev)
    calculated.append(calcMeanDev)
    print(calcMeanDev)

for i in range (0, len(calculated)):
    calculated2 = []
    if calculated[i] in range ((-3 * stDev), (3 * stDev)):
        calculated2.append(calculated[i])
    else:
        rejected = []
        rejected.append(calculated[i])

print(f'The rejected values were {rejected}')

negXAxis = ((-3 * stDev) - 5) # xMin
posXAxis = ((3 * stDev) + 5) # xMax
negYAxis = (0) # yMin
posYAxis = (100) # yMax


plt.axis([negXAxis, posXAxis, negYAxis, posYAxis])
plt.xlabel("[-3σ ; 3σ]")

print(calculated)
plt.hist(calculated2)
plt.show()