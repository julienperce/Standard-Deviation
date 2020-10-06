import main
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm


dataSet = main.dataSet
average = main.average(main.dataSet)  # mean
stDev = main.stdev # sigma
calculated = [] # list that will get appended with (dataset[i] - stDev)
accepted = []
rejected = []
confidenceLevel = 99.7

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

def marginOfError(stDev, confidenceLevel, calculated):
    standardError = (stDev / (math.sqrt(len(calculated))))
    errorMargin = standardError * confidenceLevel
    return(errorMargin)   

lower_bound = average - marginOfError(stDev, confidenceLevel, calculated) 
upper_bound = average + marginOfError(stDev, confidenceLevel, calculated) 

z1 = (lower_bound - average) / stDev # -S (neg z transform)
z2 = (upper_bound - average) / stDev # +s (pos z transform)

x = np.arange(z1, z2, 0.001) # all numbers between z1 and z2 (incremented by 0.001)
x_all = np.arange(-10, 10, 0.001) # all between -10 and 10 

y = norm.pdf(x_all, 0.1)





fig, ax = plt.subplots(figsize=(9,6))
plt.style.use('ggplot')
ax.plot(x_all,y)

plt.title("Standard Deviation graphed to a 99.7% accuracy", fontsize = 17)
plt.xlim(-4, 4)
plt.xlabel("[-3σ;  3σ]", fontsize = 14)

print(f'The accepted values were {accepted}')
print(f"Margin of error: {marginOfError(stDev, confidenceLevel, calculated)}")
print(f"Lower bound = {lower_bound} ; Upper bound = {upper_bound}")
with plt.style.context('dark_background'):
    ax.plot(x_all,y)
    plt.show()