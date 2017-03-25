from tools.display_tools import display 
from tools.process_tools import ProcessTools 
from solvers.heading_solver import HeadingSolver

def test_heading_solver():

    # Pocess the basic data 
    process = ProcessTools()
    process.load_nodes()
    process.load_ways()
    process.process_relations()

    # Start and end locations
    dalkeith_road = process.nodes['32618117']
    ivanhoe_road = process.nodes['31401881']

    # Create routing object
    solver = HeadingSolver()
    route = solver.solve(dalkeith_road,ivanhoe_road)

    display({
        'paths': [{
            'nodes': route
        }]
    })