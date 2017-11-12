from utils.neighbour_states import NEIGHBOURS
from core.coordinates import Coordinates

class Cargo:
    """ This class represents a single cargo. It contains product information, wheret it is and
        where it's going
    
        Attributes:
            product: Product description
            origin_city: The city where the product is located
            origin_state: The state where the product is located
            origin: Coordinates object containing latitude and longitude of origin
            destination_city: City where the cargo is going
            destination_state: State where the cargo is going
            destination: Coordinates of product destination
            origin_neighbour_states: List of neighbouring states of the origin state        
    
    """
    def __init__(self, product,origin_city,origin_state,origin_lat,origin_lng,
                 destination_city,destination_state,destination_lat,destination_lng):
        """Constructr for the Cargo class"""
        self.product                  = product        
        self.origin_city              = origin_city
        self.origin_state             = origin_state
        self.origin                   = Coordinates(origin_lat, origin_lng)        
        self.destination_city         = destination_city
        self.destination_state        = destination_state
        self.destination              = Coordinates(destination_lat, destination_lng)
        self.origin_neighbour_states  = NEIGHBOURS[origin_state]
