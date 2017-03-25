
class Relation:
    def __init__(self,start,end,way):
        self.bearing = start.bearing(end)
        self.distance = start.distance(end)
        self.start = start
        self.end = end
        self.way = way