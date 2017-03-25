
def bearing_fitness(route):
    return sum([
        abs(route[i].bearing(route[i+1]) - route[i+1].bearing(route[i+2]))
        for i in range(len(route)-2)
    ])

def distance_fitness(route):
    return sum([
        route[i].distance(route[i+1])
        for i in range(len(route)-1)
    ])