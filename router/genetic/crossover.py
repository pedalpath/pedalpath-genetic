def intersection(route_a,route_b):
    self_nodes = set(route_a)
    other_nodes = set(route_b)
    start_end = set([route_a[0],route_a[-1]])
    return (self_nodes & other_nodes) - start_end


def crossover(route_a,route_b):
    "perform a crossover with another route"

    offspring = []

    # Add an offspring
    def add(route):
        if (route not in offspring):
            offspring.append(route)

    # Check begining and end
    if (route_a[0] != route_b[0]):
        print('Routes do not start in the same place')
        return offspring
    if (route_a[-1] != route_b[-1]):
        print('Routes do not end in the same place')
        return offspring

    # for all intersections
    for node in intersection(route_a,route_b):
        if (len(node.neighbours) < 3): continue
        self_index = route_a.index(node)
        other_index = route_b.index(node)
        add(route_a[:self_index] + route_b[other_index:])
        add(route_b[:other_index] + route_a[self_index:])

    return offspring

# def crossover_single(route_a,route_b):

#     # Select two random routes by fitness
#     [route_a,route_b] = [ routes[i] for i in select_weighted(fitness_values,2) ]
#     # Use a crossover function to identify all potential offsprint
#     potential_offspring = [ offspring for offspring in crossover(route_a,route_b) ]

#     if (len(potential_offspring) < 3):
#         # If we only have a couple of offspring add them all
#         for offspring in potential_offspring:
#             new_routes.append(offspring)
#     else:
#         # Find the fitness of these offspring
#         offspring_fitness = [
#             offspring.fitness()
#             for offspring in potential_offspring
#         ]
#         # Add selected offspring to the routes
#         for i in select_weighted(offspring_fitness,2):
#             new_routes.append(potential_offspring[i])