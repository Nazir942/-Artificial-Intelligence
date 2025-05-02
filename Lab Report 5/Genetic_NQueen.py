import random

def create_initial_population(size, n):
    return [random.sample(range(n), n) for _ in range(size)]

def calculate_conflicts(state):
    total = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == j - i:
                total += 1
    return total

def select_parents(population, top_k):
    return sorted(population, key=calculate_conflicts)[:top_k]

def perform_crossover(a, b):
    length = len(a)
    child = [-1] * length
    start, stop = sorted(random.sample(range(length), 2))
    child[start:stop + 1] = a[start:stop + 1]

    seen = set(child[start:stop + 1])
    idx = (stop + 1) % length
    for i in range(length):
        gene = b[(stop + 1 + i) % length]
        if gene not in seen:
            child[idx] = gene
            idx = (idx + 1) % length
    return child

def mutate(solution, chance=0.1):
    if random.random() < chance:
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def solve_n_queens(n, population_size=100, max_iter=1000, elite_size=2, mutation_chance=0.1):
    population = create_initial_population(population_size, n)
    generation = 0

    while generation < max_iter:
        population.sort(key=calculate_conflicts)
        if calculate_conflicts(population[0]) == 0:
            return population[0], generation

        new_population = population[:elite_size]

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(new_population, k=2)
            child = perform_crossover(parent1, parent2)
            child = mutate(child, mutation_chance)
            new_population.append(child)

        population = new_population
        generation += 1

    population.sort(key=calculate_conflicts)
    return population[0], generation

n = 8
pop_size = 150
max_generations = 500
mutation_rate = 0.15

solution, gen = solve_n_queens(n, pop_size, max_generations, mutation_chance=mutation_rate)

if solution:
    if calculate_conflicts(solution) == 0:
        print(f"Solution found in {gen} generations:")
        print(solution)
        for r in range(n):
            row_display = ""
            for c in range(n):
                row_display += " Q" if solution[c] == r else " ."
            print(row_display)
    else:
        print(f"No perfect solution after {gen} generations.")
        print(f"Best found solution with {calculate_conflicts(solution)} conflicts:")
        print(solution)
else:
    print("Algorithm failed to return a result.")
