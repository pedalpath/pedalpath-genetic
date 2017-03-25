
class Way:
    def __init__(self,way):
        self.id = way['id']
        self.name = way['name']
        self.access = way['access']
        self.oneway = way['oneway']
        self.highway = way['highway']
        self.cycleway = way['cycleway']
        self.crossing = way['crossing']
        self.nodes = [ str(ref) for ref in way['nodes'] ]
    def adjacent_nodes(self,ref):
        "Find the references adjacent to this reference"
        index = self.nodes.index(ref)
        if (index < 0):
            return []
        elif (index is 0):
            return self.nodes[:2]
        else:
            return self.nodes[index-1:index+2]
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'access': self.access,
            'oneway': self.oneway,
            'highway': self.highway,
            'cycleway': self.cycleway,
            'crossing': self.crossing,
            'nodes': self.nodes
        }