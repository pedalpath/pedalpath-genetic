import numpy
from solvers.solver import Solver
from tools.prob_tools import select_weighted

class HeadingSolver(Solver):

    def solve(self, start, goal):

        avoid = set()
        visited = set()
        route = [start]

        def current():
            return route[-1]

        def backtrack():
            bad_node = route.pop()
            visited.remove(bad_node)
            avoid.add(bad_node)

        def move(node):
            visited.add(node)
            route.append(node)

        def select(options):
            desired_bearing = current().bearing(goal)
            bearing_differences = []
            for option in options:
                bearing_difference = numpy.radians(option.bearing-desired_bearing) % (2 * numpy.pi)
                if (bearing_difference > numpy.pi): bearing_difference -= (2 * numpy.pi)
                bearing_differences.append(bearing_difference)
            bearing_differences = numpy.array(bearing_differences)
            fitness_values = numpy.cos(bearing_differences / 2)
            options_selected = select_weighted(fitness_values)
            return options[options_selected[0]]

        while (route[-1] != goal):

            options = [
                neighbour
                for neighbour in current().neighbours
                if (
                    (neighbour.end not in avoid) and
                    (neighbour.end not in visited)
                )
            ]
            len_options = len(options)
            if (len_options == 0):
                backtrack()
            elif (len_options == 1):
                selected = options[0]
                move(selected.end)
            else:
                selected = select(options)
                move(selected.end)

        return route

