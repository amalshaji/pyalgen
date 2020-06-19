import numpy as np
#import matplotlib.pyplot as plt

class genetic_algorithm:
    def __init__(self, variables, obj_fn, population_size=1000, crossover_rate=0.25, mutation_rate=0.1):
        super().__init__()
        self.variables = variables
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.obj_fun = obj_fn

    def calculate_objective(self, pop):
        obj_values = []
        for i in pop:
            obj_values.append(self.obj_fun(*i))
        return np.array(obj_values)

    def create_population(self, var_type='int', dist_type='uniform', low=-1, high=1, mean=0, std=1):
        var_types = ['int', 'float']
        dist_types = ['uniform', 'normal']
        assert var_type in var_types
        if var_type == 'int':
            params = low, high, (self.population_size, self.variables)
            pop = np.random.randint(*params)
        else:
            assert dist_type in dist_types
            if dist_type == 'uniform':
                params = low, high, (self.population_size, self.variables)
                pop = np.random.uniform(*params)
            else:
                params = mean, std, (self.population_size, self.variables)
                pop = np.random.normal(*params)
        return pop

    def selection(self, pop, sel_type='tournament'):
        obj_val = self.calculate_objective(pop)
        fitness = 1 / (1 + obj_val)
        if sel_type.lower() == 'tournament':
            new_pop = []
            tournament_size = self.population_size
            for _ in range(tournament_size):
                random_indices = np.random.randint(1, self.population_size, 2)
                idx1 = random_indices[0]
                idx2 = random_indices[1]
                if fitness[idx1] >= fitness[idx2]:
                    new_pop.append(pop[idx1])
                else:
                    new_pop.append(pop[idx2])
        return np.array(new_pop)

    def crossover(self):
        pass

    def mutate(self):
        pass