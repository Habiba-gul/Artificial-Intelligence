import random
import math


class GA:

   
   
   
    def init(self, individualSize, populationSize):

        self.population = dict()
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.totalFitness = 0

        i = 0

        while i < populationSize:

            chromosome = list(range(individualSize))

            random.shuffle(chromosome)

            fitnessValue = self.calculateFitness(chromosome)

            self.population[i] = [chromosome, fitnessValue]

            self.totalFitness = (
                self.totalFitness + fitnessValue
            )

            i = i + 1




    def calculateFitness(self, chromosome):

        attacks = 0

        for i in range(self.individualSize):

            for j in range(i + 1, self.individualSize):

                # Diagonal Attack
                if abs(chromosome[i] - chromosome[j]) == abs(i - j):

                    attacks = attacks + 1



        fitness = 28 - attacks

        return fitness



    def updatePopulationFitness(self):

        self.totalFitness = 0

        for individual in self.population:

            chromosome = self.population[individual][0]

            fitnessValue = self.calculateFitness(chromosome)

            self.population[individual][1] = fitnessValue

            self.totalFitness = (
                self.totalFitness + fitnessValue
            )

  
  
  
  
    def selectParents(self):

        rouletteWheel = []

        wheelSize = self.populationSize * 5

        h_n = []

        for individual in self.population:

            h_n.append(
                self.population[individual][1]
            )

        j = 0

        for individual in self.population:

            if sum(h_n) == 0:

                self.individualLength = 1

            else:

                self.individualLength = round(
                    wheelSize * (h_n[j] / sum(h_n))
                )

            j = j + 1

            # Important Fix
            if self.individualLength <= 0:

                self.individualLength = 1

            i = 0

            while i < self.individualLength:

                rouletteWheel.append(individual)

                i = i + 1

        random.shuffle(rouletteWheel)

        parentIndices = []

        i = 0

        while i < self.populationSize:

            randomParent = rouletteWheel[
                random.randint(
                    0,
                    len(rouletteWheel) - 1
                )
            ]

            parentIndices.append(randomParent)

            i = i + 1

        newGeneration = dict()

        i = 0

        while i < self.populationSize:

            newGeneration[i] = (
                self.population[parentIndices[i]].copy()
            )

            i = i + 1

        self.population = newGeneration.copy()

        self.updatePopulationFitness()




    def generateChildren(self, crossoverProbability):

        numberOfPairs = round(
            crossoverProbability *
            self.populationSize / 2
        )

        i = 0
        j = 0

        while i < numberOfPairs:

            crossoverPoint = random.randint(
                1,
                self.individualSize - 2
            )

            parent1 = self.population[j][0]

            parent2 = self.population[j + 1][0]

            child1 = parent1[0:crossoverPoint]

            child2 = parent2[0:crossoverPoint]

            # Fill remaining values
            for gene in parent2:

                if gene not in child1:

                    child1.append(gene)

            for gene in parent1:

                if gene not in child2:

                    child2.append(gene)

            self.population[j] = [
                child1,
                self.calculateFitness(child1)
            ]

            self.population[j + 1] = [
                child2,
                self.calculateFitness(child2)
            ]

            i = i + 1
            j = j + 2

        self.updatePopulationFitness()

    
    
    
    def mutateChildren(self, mutationProbability):

        numberOfMutations = round(
            mutationProbability *
            self.populationSize
        )

        i = 0

        while i < numberOfMutations:

            individualIndex = random.randint(
                0,
                self.populationSize - 1
            )

            chromosome = (
                self.population[individualIndex][0]
            )

            # Swap Mutation
            pos1 = random.randint(
                0,
                self.individualSize - 1
            )

            pos2 = random.randint(
                0,
                self.individualSize - 1
            )

            chromosome[pos1], chromosome[pos2] = (
                chromosome[pos2],
                chromosome[pos1]
            )

            self.population[individualIndex] = [
                chromosome,
                self.calculateFitness(chromosome)
            ]

            i = i + 1

        self.updatePopulationFitness()

    # --------------------------------
    # Print Chess Board
    # --------------------------------
    def printBoard(self, chromosome):

        print("\nCorrect 8-Queen Board:\n")

        for row in range(8):

            for col in range(8):

                # Queen Position
                if chromosome[col] == row:

                    print("Q", end=" ")

                else:

                    # Chess Pattern
                    if (row + col) % 2 == 0:

                        print("-", end=" ")

                    else:

                        print(".", end=" ")

            print()



def main():

    print("Program Started")

    individualSize = 8

    populationSize = 100

    generation = 0

    maxGenerations = 1000

    instance = GA()

    instance.init(
        individualSize,
        populationSize
    )

    while generation < maxGenerations:

        instance.selectParents()

        instance.generateChildren(0.8)

        instance.mutateChildren(0.2)

        print("\nGeneration =", generation)

        bestFitness = 0

        for individual in instance.population:

            chromosome = (
                instance.population[individual][0]
            )

            fitness = (
                instance.population[individual][1]
            )

            print(
                "Chromosome:",
                chromosome,
                " Fitness:",
                fitness
            )

            if fitness > bestFitness:

                bestFitness = fitness

        print("\nBest Fitness =", bestFitness)

        found = False

        for individual in instance.population:

            if (
                instance.population[individual][1]
                == 28
            ):

                found = True

                solution = (
                    instance.population[individual][0]
                )

                print("\nSolution Found!")

                print(
                    "\nChromosome =",
                    solution
                )

                instance.printBoard(solution)

                break

        if found:

            break

        generation = generation + 1

    if not found:

        print(
            "\nSolution not found within generation limit."
        )



if __name__ == "__main__":

    main()