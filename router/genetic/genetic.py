from tools.display_tools import display 
from tools.prob_tools import select_weighted 
from tools.process_tools import ProcessTools 
from solvers.heading_solver import HeadingSolver

from genetic.crossover import crossover
from genetic.fitness import bearing_fitness,distance_fitness
from genetic.mutation import mutate_section,mutate_start,mutate_end

class Solution():
    def __init__(self,route):
        self.route = route
    def to_json(self):
        return { 'nodes': self.route }

class Genetic:

    def __init__(self,
            solver=HeadingSolver(),
            fitness_functions=[{'weight': 1,'function': distance_fitness}]
        ):

        self.solver = solver
        self.fitness_functions = fitness_functions


    def _route_fitness(self,route):
        return sum([
            fitness_function['weight'] * fitness_function['function'](route)
            for fitness_function in self.fitness_functions
        ])

    # Create a new list of routes
    def _select_solutions(self,solutions,number):
        fitness_probabilities = [ 1/solutions[0].fitness for solution in solutions ]
        solution_indexs = select_weighted(fitness_probabilities,number)
        return [ solutions[solution_index] for solution_index in solution_indexs ]

    def solve(self,start,end):

        # Find solution
        routes = []
        num_epoc = 100
        num_routes = 10
        num_mutations = 2
        num_crossovers = 2

        # Find 20 random routes
        print('Finding inital random solutions')
        for i in range(num_routes):
            route = self.solver.solve(start,end)
            routes.append(route)

        # For 10 itterations select best routes
        fitness = []
        for i in range(num_epoc):

            # Create solutions
            solutions = []
            for route in routes:
                solution = Solution(route)
                solution.fitness = self._route_fitness(route)
                solutions.append(solution)

            # Sort solutions by fitness
            solutions.sort(key=lambda solution:solution.fitness)
            yield solutions

            # Select members of the population randomly to mutate
            mutations = []
            for solution in self._select_solutions(solutions,10):
                route = mutate_start(solution.route)
                solution = Solution(route)
                solution.fitness = self._route_fitness(route)
                mutations.append(solution)
                route = mutate_end(solution.route)
                solution = Solution(route)
                solution.fitness = self._route_fitness(route)
                mutations.append(solution)

            # Select members of the population randomly to crossover
            offspring = []
            for solution in self._select_solutions(solutions,10):
                for route in crossover(solution.route):
                    solution = Solution(route)
                    solution.fitness = self._route_fitness(route)
                    offspring.append(solution)

            # Select members of population to randomly kill
            fitness_probabilities = [ solution.fitness - solutions[0].fitness for solution in solutions ]
            removed_solution_indexs = select_weighted(fitness_probabilities,20)

            # Routes
            routes = [
                solution
                for index,solution in enumerate(
                    solutions +
                    self._select_solutions(mutations,10) +
                    self._select_solutions(offspring,10)
                )
                if (index not in removed_solution_indexs)
            ]


def main():

    # Pocess the basic data 
    process = ProcessTools()
    process.load_nodes()
    process.load_ways()
    process.process_relations()

    # Start and end locations
    dalkeith_road = process.nodes['32618117']
    ivanhoe_road = process.nodes['31401881']

    # Modified fitness functions
    fitness_functions = [{
        'weight': 0.8,
        'function': distance_fitness
    },{
        'weight': 0.2,
        'function': bearing_fitness
    }]

    # Solve genetic algorithm
    fitness = []
    genetic = Genetic(fitness_functions=fitness_functions)
    for solutions in genetic.solve(dalkeith_road,ivanhoe_road):
        fitness.append(solutions[0].fitness)
        display({ 'paths': solutions[:2] })

    # plot fitness values
    plot(range(len(fitness)),fitness)


