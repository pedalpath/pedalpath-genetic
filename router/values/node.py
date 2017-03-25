from tools.geom_tools import GeomTools

geom_tools = GeomTools()

class Node:
    def __init__(self,node):
        self.ref = node['ref']
        self.lat = node['lat']
        self.lon = node['lon']
        # ways that pass through this node
        self.ways = node['ways']
        # neighbouring nodes to this node
        self.neighbours = []
    def bearing(self,other):
        return geom_tools.calculate_bearing(
            [self.lat,self.lon],
            [other.lat,other.lon]
        )
    def distance(self,other):
        return geom_tools.calculate_distance(
            [self.lat,self.lon],
            [other.lat,other.lon]
        )
    def __hash__(self):
        return hash(self.ref)
    def __repr__(self):
        return '[{},{}]'.format(self.lat,self.lon)
    def to_json(self):
        return {
            'ref': self.ref,
            'lat': self.lat,
            'lon': self.lon,
            'ways': self.ways
        }
