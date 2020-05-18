import random, math


def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for i in range(n)]


def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i + 1) * numberList[i] ** 2
    return sum


def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def Annealing(Function, leftEnd, rightEnd, dimension, searchingMinimum=True):
    coolingCoefficient = 0.9
    absoluteTemperature = 1000
    iterations = 1000

    bestVector = RandomNumbers(leftEnd, rightEnd, dimension)
    bestFitness = Function(bestVector)
    currentTemperature = absoluteTemperature

    for i in range(iterations):
        for j in range(50):

            newVector = bestVector[:]
            k = random.randint(0, dimension - 1)
            newVector[k] += 0.001 * random.uniform(leftEnd, rightEnd)
            newVector[k] = max(min(newVector[k], rightEnd), leftEnd)
            newFitness = Function(newVector)

            if searchingMinimum == True:
                if newFitness > bestFitness:
                    delta = newFitness - bestFitness
                    probability = math.exp(-delta / currentTemperature)
                    if random.random() > probability:
                        continue
            else:
                if newFitness < bestFitness:
                    delta = newFitness - bestFitness
                    probability = math.exp(delta / currentTemperature)
                    if random.random() > probability:
                        continue

            bestVector = newVector
            bestFitness = Function(bestVector)

        currentTemperature *= coolingCoefficient

    for x in range(len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
          "\n f(x) =", round(bestFitness, 5), "\n")


Annealing(Sum_Squares, -10, 10, 5, True)
Annealing(Weierstrass, -10, 10, 5, True)
Annealing(Sum_Squares, -10, 10, 5, False)
Annealing(Weierstrass, -10, 10, 5, False)
