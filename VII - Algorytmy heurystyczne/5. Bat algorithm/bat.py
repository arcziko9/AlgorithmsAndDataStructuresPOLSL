import random


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


class Bat(object):
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0] * len(position)


def BatAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum=True):
    generationCount = 500
    populationCount = 100
    freqMin = 0.0
    freqMax = 2.0
    loudness = 0.5
    pulseRate = 0.5
    epsilon = 0.001

    population = [Bat(RandomNumbers(leftEnd, rightEnd, dimension)) for i in
                  range(populationCount)]

    population.sort(key=lambda x: Function(x.position))
    if searchingMinimum == False: population.reverse()
    leaderPosition = population[0].position[:]

    t = 0
    while t <= generationCount:
        for bat in population:
            pulsation = freqMin + (freqMax - freqMin) * random.random()
            newPosition = bat.position[:]
            for k in range(dimension):
                bat.velocity[k] += (bat.position[k] - leaderPosition[k]) * pulsation
                newPosition[k] = max(min(newPosition[k] + bat.velocity[k], rightEnd), leftEnd)

            if random.random() > pulseRate:
                for k in range(dimension):
                    newPosition[k] = leaderPosition[k] + epsilon * random.normalvariate(0, 1)
                    newPosition[k] = max(min(newPosition[k], rightEnd), leftEnd)

            if searchingMinimum == True:
                if Function(newPosition) <= Function(bat.position) and random.random() < loudness:
                    bat.positon = newPosition[:]
                if Function(newPosition) <= Function(leaderPosition):
                    leaderPosition = newPosition[:]
            else:
                if Function(newPosition) >= Function(bat.position) and random.random() < loudness:
                    bat.positon = newPosition[:]
                if Function(newPosition) >= Function(leaderPosition):
                    leaderPosition = newPosition[:]

        t += 1

    bestVector = leaderPosition
    for x in range(len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
          "\n f(x) =", round(Function(bestVector), 5), "\n")


BatAlgorithm(Sum_Squares, -10, 10, 5, True)
BatAlgorithm(Weierstrass, -10, 10, 5, True)
BatAlgorithm(Sum_Squares, -10, 10, 5, False)
BatAlgorithm(Weierstrass, -10, 10, 5, False)
