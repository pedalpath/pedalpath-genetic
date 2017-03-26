import random
import numpy.random

def select(options):
    return random.choice(options)

def select_weighted(fitness_values,number_of_items_to_pick=1):
    list_of_candidates = range(len(fitness_values))
    probability_distribution = numpy.array(fitness_values) / numpy.sum(fitness_values)
    selection = numpy.random.choice(list_of_candidates, number_of_items_to_pick, p=probability_distribution, replace=False)
    return selection