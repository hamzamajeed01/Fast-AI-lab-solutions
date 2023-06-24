#write a python program to solve 8 queen problem using genetic algorithm

import random
import sys
import math
import copy

#function to generate random population
def generatePopulation(populationSize,chromosomeSize):
    population = []
    for i in range(populationSize):
        chromosome = []
        for j in range(chromosomeSize):
            chromosome.append(random.randint(0,chromosomeSize-1))
        population.append(chromosome)
    return population

#function to calculate fitness of each chromosome
def calculateFitness(population):
    fitness = []
    for i in range(len(population)):
        horizontalCollisions = sum([population[i].count(queen)-1 for queen in population[i]])/2
        diagonalCollisions = 0
        n = len(population[i])
        leftDiagonal = [0] * 2*n
        rightDiagonal = [0] * 2*n
        for i in range(n):
            leftDiagonal[i + population[i][i] - 1] += 1
            rightDiagonal[len(population[i]) - i + population[i][i] - 2] += 1
        diagonalCollisions = 0
        for i in range(2*n-1):
            counter = 0
            if leftDiagonal[i] > 1:
                counter += leftDiagonal[i]-1
            if rightDiagonal[i] > 1:
                counter += rightDiagonal[i]-1
            diagonalCollisions += counter / (n-abs(i-n+1))
        fitness.append(int(maxFitness - (horizontalCollisions + diagonalCollisions)))
    return fitness

#function to select parents for crossover
def selection(population,fitness):
    newPopulation = []
    for i in range(len(population)):
        chromosome1 = random.choices(population,weights=fitness,k=1)
        chromosome2 = random.choices(population,weights=fitness,k=1)
        newPopulation.append(crossover(chromosome1[0],chromosome2[0]))
    return newPopulation

#function to perform crossover
def crossover(chromosome1,chromosome2):
    newChromosome = []
    crossoverPoint = random.randint(0,len(chromosome1)-1)
    for i in range(len(chromosome1)):
        if i > crossoverPoint:
            newChromosome.append(chromosome1[i])
        else:
            newChromosome.append(chromosome2[i])
    return newChromosome

#function to perform mutation
def mutation(population):
    for i in range(len(population)):
        if random.random() < mutationRate:
            randomValue = random.randint(0,len(population[i])-1)
            population[i][randomValue] = random.randint(0,len(population[i])-1)
    return population

#function to check if solution is found
def checkSolution(population):
    solutions = []
    for i in range(len(population)):
        if fitness[i] == maxFitness:
            solutions.append(population[i])
    return solutions

#function to print the board
def printBoard(chromosome):
    print('-----------------')
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if chromosome[j] == i:
                print('Q',end='')
            else:
                print('-',end='')
        print('-',end='')
        for j in range(len(chromosome)):
            if chromosome[j] == i:
                print('Q')
            else:
                print('-')
        print('-----------------')

#main function
if __name__ == '__main__':
    #input
    populationSize = int(input('Enter population size: '))
    chromosomeSize = int(input('Enter chromosome size: '))
    mutationRate = float(input('Enter mutation rate: '))
    maxFitness = (chromosomeSize*(chromosomeSize-1))/2
    population = generatePopulation(populationSize,chromosomeSize)
    fitness = calculateFitness(population)
    solutions = checkSolution(population)
    generation = 1
    while solutions == []:
        print('Generation: ',generation)
        print('Population: ',population)
        print('Fitness: ',fitness)
        print('Solutions: ',solutions)
        print(' ')
        population = selection(population,fitness)
        population = mutation(population)
        fitness = calculateFitness(population)
        solutions = checkSolution(population)
        generation += 1
    print('Generation: ',generation)
    print('Population: ',population)
    print('Fitness: ',fitness)
    print('Solutions: ',solutions)
    print(' ')
    print('Solution found in generation ',generation-1)
    printBoard(solutions[0])

