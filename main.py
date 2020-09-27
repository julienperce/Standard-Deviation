import math

print("Welcome to the standard deviation calculator!")
dataSet = list(map(float,input("Enter your dataset, seperated by spaces. Press enter when done: ").strip().split()))
print(dataSet, len(dataSet))

def average(dataSet):
    dataSetNum = 0
    for i in range (0, len(dataSet)):
        dataSetNum += dataSet[i]
    return float(dataSetNum / len(dataSet))

def epsilon(dataSet):
    bases = []
    for i in range (0, len(dataSet)):
        bases.append(((dataSet[i] - average(dataSet))**2))
    return sum(bases)

def fraction(dataSet):
    return (epsilon(dataSet) / len(dataSet))

print(f"The average of your dataset is: {average(dataSet)}")
print(f"The standard deviation of your dataset is: {math.sqrt(fraction(dataSet))}")
