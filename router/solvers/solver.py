class Solver:

    def heuristic_cost_estimate(self, node1, node2):
        """computes the estimated (rough) distance between two random nodes, this method must be implemented in a subclass
        computes the 'direct' distance between two (x,y) tuples"""

        return node1.distance(node2)

    def distance_between(self, node1, node2):
        """gives the real distance between two adjacent nodes n1 and n2 (i.e n2 belongs to the list of n1's neighbors), this method must be implemented in a subclass
        this method always returns 1, as two 'neighbors' are always adajcent"""

        # This will use more complex aspects in the future
        return node1.distance(node2)

    def neighbors(self, node):
        """for a given node, returns (or yields) the list of its neighbors. this method must be implemented in a subclass
        for a given coordinate in the maze, returns up to 4 adjacent nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        
        return [ neighbor.end for neighbor in node.neighbors ]