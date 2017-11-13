from utils.us_states import NEIGHBOURS
from core.coordinates import Coordinates

class Cargo(object):
    """ This class represents a single cargo. It contains product information, where it is and
        where it's going
    
        Attributes:
            product: Product description
            origin_city: The city where the product is located
            origin_state: The state where the product is located
            origin: Coordinates object containing latitude and longitude of origin
            destination_city: City where the cargo is going
            destination_state: State where the cargo is going
            destination: Coordinates of product destination
    """
    def __init__(self, product,origin_city,origin_state,origin_lat,origin_lng,
                 destination_city,destination_state,destination_lat,destination_lng):
        """Constructor for the Cargo class"""
        self.product             = product        
        self.origin_city         = origin_city
        self._origin_state       = origin_state
        self.origin              = Coordinates(origin_lat, origin_lng)        
        self.destination_city    = destination_city
        self._destination_state  = destination_state
        self.destination         = Coordinates(destination_lat, destination_lng)

    @property
    def origin_state(self):
        return self._origin_state

    @origin_state.setter
    def origin_state(self, value):
        """Setter method for the origin US state info

        Args:
            value: Valid US State

        Raises:
            InvalidUSState: The state given does not belog to the US
        """
        if value not in NEIGHBOURS:
            raise InvalidUSState("Given state does not belong to the United States")
        self._origin_state = value

    @property
    def destination_state(self):
        return self._destination_state

    @destination_state.setter
    def destination_state(self, value):
        """Setter method for the destination US state info

        Args:
            value: Valid US State

        Raises:
            InvalidUSState: The state given does not belog to the US
        """
        if value not in NEIGHBOURS:
            raise InvalidUSState("Given state does not belong to the United States")
        self._destination_state = value
