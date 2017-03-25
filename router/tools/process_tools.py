from tools.utilities import load
from values.way import Way
from values.node import Node
from values.relation import Relation

class ProcessTools:

    def load_nodes(self,filename='data/dulwich_nodes.json'):
        self.nodes = {
            ref: Node(node)
            for (ref, node) in load(filename).items()
        }

    def load_ways(self,filename='data/dulwich_ways.json'):
        self.ways = [
            Way(way)
            for way in load(filename)
        ] 

    def process_relations(self):

        # Find adjacent nodes to one and other
        for (ref,node) in self.nodes.items():
            node.neighbours = []
            for way_id in node.ways:
                if (way_id > len(self.ways)):
                    continue
                way = self.ways[way_id]
                for _ref in way.adjacent_nodes(ref):
                    if (ref == _ref): continue
                    if (_ref in self.nodes):           
                        _node = self.nodes[_ref]
                        neighbour = Relation(node,_node,way)
                        node.neighbours.append(neighbour)