import random
from solvers.heading_solver import HeadingSolver

def mutate_section(route,start_index,end_index,solver=HeadingSolver()):
    route_section = solver.solve(route[start_index],route[end_index])
    return route[:start_index] + route_section + route[end_index:]

def mutate_start(route,solver=HeadingSolver()):
    node_index = random.randint(0,len(route)-1)
    route_begining = solver.solve(route[0],route[node_index])
    return route_begining + route[node_index:]

def mutate_end(route,solver=HeadingSolver()):
    node_index = random.randint(0,len(route)-1)
    route_ending = solver.solve(route[node_index],route[-1])
    return route[:node_index] + route_ending