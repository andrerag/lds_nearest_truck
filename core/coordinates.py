import math

class InvalidCoordinate(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Coordinates(object):
    """Contains lattitude and longitude information
    
    This class is not just a C-like struct object. The Coordinates class is also able to
    calculate the distance from it's lat, lng information to another Coordinates object.

    Attributes:
        lat: Object's lattitude
        lng: Object's longitude

    """
    def __init__(self, lat, lng):
        """Constructor for the Coordinates class"""
        self.lat = lat
        self.lng = lng
    
    def distance_to(self, coordinates):
        """Calculates the distance to another Coordinates object

        Args:
            coordinates: Coordinates object to measure distance to.
        """
        return self.__haversine_distance(coordinates)

    def __haversine_distance(self, coordinates):
        """Calculates distance using the haversine formula

            This function calculates distance using latitude and longitude information using the
            haversine formula, which taks into account the earth's curvature.

            Args:
                coordinates: Coordinates object to measure distance to.

            Returns:
                Distance in Km to given Coordinates object
        """
        earth_radius = float(6371e3)
        phi1 = math.radians(coordinates.lat)
        phi2 = math.radians(self.lat)        
        delta_phi = math.radians(coordinates.lat - self.lat)
        delta_lambda = math.radians(coordinates.lng - self.lng)
        
        halfchord_square = math.sin(delta_phi/2) * math.sin(delta_phi/2) +\
                           math.cos(phi1) * math.cos(phi2) *\
                           math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
            
        angular_distance = 2 * math.atan2(math.sqrt(halfchord_square), math.sqrt(1 - halfchord_square))
        
        return (earth_radius * angular_distance)

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        """Setter method for lattitude value
        
        Args:
            value: Latitude value must be in the interval: -90 <= value <= +90

        Raises:
            InvalidCoordinates: An invalid lattitude was given
        """
        fvalue = float(value)
        if fvalue < -90. or fvalue > 90:
            raise InvalidCoordinate("Latitude value not valid (90 <= lat <= 90)")
        self._lat = fvalue

    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        """Setter method for longitude value

        Args:
            value: Longitude value must be in the interval: -180 <= value <= 180

        Raises:
            InvalidCoordinates: An invalid longitude value was given
        """        
        fvalue = float(value)
        if fvalue < -180. or fvalue > 180.:
            raise InvalidCoordinate("Longitude value not valid (-180 <= lat <= 180)")
        self._lng = fvalue