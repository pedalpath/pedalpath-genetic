import math

class GeomTools:

    R = 6378137

    def calculate_offset(self,coordinate_a,coordinate_b):
        """Find the horizontal and vertical offset between coordinates"""

        [lat_a,lng_a] = coordinate_a
        [lat_b,lng_b] = coordinate_b

        x = math.pi * self.R * (lng_b - lng_a) * math.cos( math.pi * lat_a / 180 ) / 180
        y = math.pi * self.R * (lat_b - lat_a) / 180

        return [x,y]

    def calculate_distance(self,coordinate_a,coordinate_b):

        offset = self.calculate_offset(coordinate_a,coordinate_b)
        return math.sqrt(offset[0]**2+offset[1]**2)

    def calculate_bearing(self,pointA, pointB):
        """
        Calculates the bearing between two points.
        The formulae used is the following:
            θ = atan2(sin(Δlong).cos(lat2),
                      cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
        :Parameters:
          - `pointA: The tuple representing the latitude/longitude for the
            first point. Latitude and longitude must be in decimal degrees
          - `pointB: The tuple representing the latitude/longitude for the
            second point. Latitude and longitude must be in decimal degrees
        :Returns:
          The bearing in degrees
        :Returns Type:
          float
        """

        lat1 = math.radians(pointA[0])
        lat2 = math.radians(pointB[0])

        diffLong = math.radians(pointB[1] - pointA[1])

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(x, y)

        # Now we have the initial bearing but math.atan2 return values
        # from -180° to + 180° which is not what we want for a compass bearing
        # The solution is to normalize the initial bearing as shown below
        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        return compass_bearing

    def calculate_coordinate(self,coordinate,offset):
        """Find the coordinate offset by given amount from coordinate"""

        [lat_a,lng_a] = coordinate
        [x,y] = offset

        lat_b = lat_a + 180 * y / ( math.pi * self.R )
        lng_b = lng_a + 180 * x / ( math.pi * self.R * math.cos( math.pi * lat_a / 180 ) )

        return [lat_b,lng_b]

    def convert_coordinates_to_offsets(self,reference,coordinates):
        """Find all offsets for given coordinates from reference"""

        return [
            self.calculate_offset(reference,coordinate)
            for coordinate in coordinates
        ]

    def convert_offsets_to_coordinates(self,reference,offsets):
        """Find all coordinates for given offsets from reference"""

        return [
            self.calculate_coordinate(reference,offset)
            for offset in offsets
        ]


if (__name__ == "__main__"):

    geom_tools = GeomTools()
    offset = geom_tools.calculate_offset((41.49008, -71.312796),(41.499498, -81.695391))
    print(offset,math.sqrt(offset[0]**2+offset[1]**2))
    coordinate = geom_tools.calculate_coordinate((41.49008, -71.312796),offset)
    print(coordinate)
