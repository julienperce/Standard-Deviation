import math
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm

print("Welcome to the standard deviation calculator!")
def datasetGenerate():
    randomQuery = str(input("Would you like a random dataset? Type 1 or yes if yes, else type no: "))
    if randomQuery.lower() == "1" or randomQuery.lower() == "yes":
        setMin = int(input("Enter the minimum value of dataset: "))
        setMax = int(input("Enter the maximum value of dataset: "))
        size = int(input("Enter the size of your dataset: "))
        i = setMin
        dataSet = []
        for i in range (0, size):
            randChoice = random.randint(setMin, setMax)
            dataSet.append(randChoice)
        print(f'Your dataset was created.') # with a length of {size}: {dataSet}')
    else:
        dataSet = list(map(float,input("Enter your dataset - seperate the values by spaces. Press enter when done: ").strip().split()))
    return dataSet

def average(dataSet): # the average of the dataset
    dataSetNum = 0 
    for i in range (0, len(dataSet)):
        dataSetNum += dataSet[i]
    return float(dataSetNum / len(dataSet))

def epsilon(dataSet, average): # The distance between each datapoint and the mean, and then squared
    bases = []
    for i in range (0, len(dataSet)):
        base = (dataSet[i] - average)**2
        bases.append(base)
    return sum(bases)

def fraction(dataSet):
    return (epsilon(dataSet, average) / len(dataSet))

def graphDev(dataSet, average):  # mean
    print("Graphing...")
    calculated = [] # list that will get appended with (dataset[i] - stDev)
    accepted = []
    rejected = []
    confidenceLevel = 99.7

    for i in range (0, len(dataSet)):
        calcMeanDev = float(dataSet[i] - stDev)
        calculated.append(calcMeanDev)

    for i in range (0, len(calculated)):
        if calculated[i] >= (-3 * stDev) and calculated[i] <= (3 * stDev):
            accepted.append(calculated[i])
        else:
            rejected.append(calculated[i])

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

    print(f"Margin of error: {marginOfError(stDev, confidenceLevel, calculated)}")
    print(f"Lower bound = {lower_bound} ; Upper bound = {upper_bound}")
    with plt.style.context('dark_background'):
        ax.plot(x_all,y)
        plt.show()

if __name__ == "__main__":
    calculated = [] # list that will get appended with (dataset[i] - stDev)
    accepted = []
    rejected = []
    confidenceLevel = 99.7
    dataSet = datasetGenerate()
    average = average(dataSet)
    stDev = math.sqrt(fraction(dataSet))
    print(f"The average of your dataset is: {average}")
    print(f"The standard deviation of your dataset is: {stDev}")
    graphDev(dataSet, average)