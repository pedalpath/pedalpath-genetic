class Solver:

    def __init__(self, nodes):
        self.nodes = nodes

    def heuristic_cost_estimate(self, node1, node2):
        """computes the estimated (rough) distance between two random nodes, this method must be implemented in a subclass
        computes the 'direct' distance between two (x,y) tuples"""
        # (x1, y1) = n1
        # (x2, y2) = n2
        # return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance_between(self, node1, node2):
        """gives the real distance between two adjacent nodes n1 and n2 (i.e n2 belongs to the list of n1's neighbors), this method must be implemented in a subclass
        this method always returns 1, as two 'neighbors' are always adajcent"""
        # return 1



    def neighbors(self, node):
        """for a given node, returns (or yields) the list of its neighbors. this method must be implemented in a subclass
        for a given coordinate in the maze, returns up to 4 adjacent nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        for i, j in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x1 = x + i
            y1 = y + j
            if x1 > 0 and y1 > 0 and x1 < self.width and y1 < self.height:
                if self.lines[y1][x1] == ' ':
                    yield (x1, y1)