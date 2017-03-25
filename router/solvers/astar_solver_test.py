from tools.display_tools import display 
from tools.process_tools import ProcessTools 
from solvers.astar_solver import AStarSolver

def test_astar_solver():

    # Pocess the basic data 
    process = ProcessTools()
    process.load_nodes()
    process.load_ways()
    process.process_relations()

    # Start and end locations
    dalkeith_road = process.nodes['32618117']
    ivanhoe_road = process.nodes['31401881']

    # Create routing object
    solver = AStarSolver()
    route = solver.solve(dalkeith_road,ivanhoe_road)

    display({
        'paths': [{
            'nodes': route
        }]
    })