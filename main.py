import math
import random

print("Welcome to the standard deviation calculator!")
randomQuery = input("Would you like a random dataset? Type 1 if yes, Type 2 if no: ")
if randomQuery == "1" or randomQuery == 1:
    setMin = int(input("Enter the minimum value of dataset: "))
    setMax = int(input("Enter the maximum value of dataset: "))
    size = int(input("Enter the size of your dataset: "))
    i = setMin
    dataSet = []
    for i in range (0, size):
        randChoice = random.randint(setMin, setMax)
        dataSet.append(randChoice)
    print(f'Your dataset was created, with a length of {size}: {dataSet}')
else:
    dataSet = list(map(float,input("Enter your dataset, seperated by spaces. Press enter when done: ").strip().split()))

def average(dataSet): # the average of the dataset
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

stdev = math.sqrt(fraction(dataSet))

print(f"The average of your dataset is: {average(dataSet)}")
print(f"The standard deviation of your dataset is: {stdev}")
