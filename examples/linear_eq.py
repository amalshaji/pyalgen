import pyalgen

pop = pyalgen.Population(1, 30, unique=True, dtype='int')
population = pop(1000, 4)
# print(population)
selection = pyalgen.Selection.tournament
crossover = pyalgen.Crossover.onepoint
mutation = pyalgen.Mutation.randompoint

def obj(a, b, c, d):
    return a + 2*b + 3*c + 4*d - 30

ga = pyalgen.GeneticAlgorithm(population, obj, selection, crossover, mutation)


iterations, objective, pop = ga.forward(iterations=1000)

if iterations == 1000:
    print(f'min_value: {objective.min()}, solution: {pop[objective.argmin()]}, generation: {iterations}')   
else:
    print(f'min_value: {objective[objective == 0][0]}, solution: {pop[objective == 0][0]}, generation: {iterations}')   