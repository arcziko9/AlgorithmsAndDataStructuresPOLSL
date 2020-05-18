import random, math


def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]


def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i + 1) * numberList[i] ** 2
    return sum


def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def calculateDistance(one, two):
    distance = 0
    for k in range(len(one)): distance += (one[k] - two[k]) ** 2
    distance **= 0.5
    return distance


class Firefly(object):
    def __init__(self, position):
        self.position = position


def FireflyAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum=True):
    generationCount = 300
    populationCount = 20
    absorptionRatio = 0.01
    attractZero = 0.01
    randomRatio = 0.01
    population = [Firefly(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)]

    t = 0
    while t <= generationCount:
        for i in range(populationCount):
            for j in range(populationCount):

                iPos = population[i].position
                jPos = population[j].position
                distance = calculateDistance(iPos, jPos)
                attr = attractZero * math.exp(-absorptionRatio * distance ** 2)

                candidatePos = iPos[:]
                for k in range(dimension):
                    candidatePos[k] += attr * (jPos[k] - iPos[k]) + random.normalvariate(0, 1) * randomRatio
                    candidatePos[k] = max(min(candidatePos[k], rightEnd), leftEnd)
                if searchingMinimum == True and Function(candidatePos) < Function(population[i].position):
                    population[i].position = candidatePos
                elif searchingMinimum == False and Function(candidatePos) > Function(population[i].position):
                    population[i].position = candidatePos
        t += 1

    population.sort(key=lambda x: Function(x.position))
    if searchingMinimum == False: population.reverse()
    bestVector = population[0].position[:]
    for x in range(len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
          "\n f(x) =", round(Function(bestVector), 5), "\n")


FireflyAlgorithm(Sum_Squares, -10, 10, 5, True)
FireflyAlgorithm(Weierstrass, -10, 10, 5, True)
FireflyAlgorithm(Sum_Squares, -10, 10, 5, False)
FireflyAlgorithm(Weierstrass, -10, 10, 5, False)
