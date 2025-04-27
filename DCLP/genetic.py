import random

class Chromosome:
    def __init__(self, k):
        self.k = k
        self.genes = [random.randint(0, 9) for _ in range(k)]
        self.fitness = 0

    def evaluate_fitness(self, target):
        self.fitness = -abs(target - sum(self.genes))

class Population:
    def __init__(self, size, k, target):
        self.size = size
        self.k = k
        self.target = target
        self.chromosomes = [Chromosome(k) for _ in range(size)]
        self.best_chromosome = None

    def initialize(self):
        self.chromosomes = [Chromosome(self.k) for _ in range(self.size)]

    def evaluate_fitness(self):
        for chromosome in self.chromosomes:
            chromosome.evaluate_fitness(self.target)
        self.best_chromosome = max(self.chromosomes, key=lambda chrom: chrom.fitness)

    def get_best_chromosome(self):
        return self.best_chromosome

    def get_second_best_chromosome(self):
        sorted_chromosomes = sorted(self.chromosomes, key=lambda chrom: chrom.fitness, reverse=True)
        return sorted_chromosomes[1]

    def get_least_fit_index(self):
        least_fit_index = min(range(self.size), key=lambda i: self.chromosomes[i].fitness)
        return least_fit_index

class GeneticAlgorithm:
    def __init__(self, target, k):
        self.target = target
        self.k = k
        self.population = Population(10, k, target)
        self.best_chromosome = None
        self.second_best_chromosome = None
        self.generation_count = 0

    def select_parents(self):
        self.best_chromosome = self.population.get_best_chromosome()
        self.second_best_chromosome = self.population.get_second_best_chromosome()

    def crossover_parents(self):
        crossover_point = random.randint(1, self.k - 1)
        for i in range(crossover_point):
            self.best_chromosome.genes[i], self.second_best_chromosome.genes[i] = self.second_best_chromosome.genes[i], self.best_chromosome.genes[i]

    def mutate_chromosomes(self):
        mutation_point = random.randint(0, self.k - 1)
        self.best_chromosome.genes[mutation_point] = random.randint(0, 9)
        mutation_point = random.randint(0, self.k - 1)
        self.second_best_chromosome.genes[mutation_point] = random.randint(0, 9)

    def replace_least_fit_chromosome(self):
        self.best_chromosome.evaluate_fitness(self.target)
        self.second_best_chromosome.evaluate_fitness(self.target)
        offspring = self.best_chromosome if self.best_chromosome.fitness > self.second_best_chromosome.fitness else self.second_best_chromosome
        index = self.population.get_least_fit_index()
        self.population.chromosomes[index] = offspring

    def run(self):
        self.population.initialize()
        self.population.evaluate_fitness()

        while sum(self.population.get_best_chromosome().genes) != self.target:
            self.generation_count += 1
            self.select_parents()
            self.crossover_parents()
            if random.randint(0, 6) < 5:
                self.mutate_chromosomes()
            self.replace_least_fit_chromosome()
            self.population.evaluate_fitness()

        result = self.population.get_best_chromosome().genes
        print("Solution found:", *result)

if __name__ == "__main__":
    target = int(input("Enter the value of Target: "))
    length = int(input("Enter the Length of the list: "))
    ga = GeneticAlgorithm(target, length)
    ga.run()
