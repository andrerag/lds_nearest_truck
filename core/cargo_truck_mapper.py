from collections import defaultdict

from core.truck_locator import TruckLocator
from core.trucks import Truck
from core.cargo  import Cargo

class CargoTruckMapper:
    def __init__(self, cargo_list, trucks_bystate):
    	"""Constructor for the CargoTruckMapper

    	Attributes:
    		cargo_list: List of cargos to mapped with nearest trucks
    		trucks_bystate: List of trucks sorted by state
    	"""
        self._cargo_list = cargo_list
        self._trucks_bystate = trucks_bystate

    def map_cargos_to_trucks(self):
        """Maps cargos to trucks

        This fuction goes through the cargo list and finds the appropriate truck for it. The appropriate
        truck for a given cargo is the nearest truck possible in a way that it assures that the distance
        travelled by all trucks is the minimum possible. This function also checks if a truck was
        assigned to more than one cargo, if that happens, the function calls remove_duplicates() in
        order to fix the issue.

        Returns:
            A list tuple of the cargos and their respective trucks. Currently the list has the
            following structure:

            [(Cargo Object, Truck Object, Distance to Truck)]
        """
        truck_locator = TruckLocator(self._trucks_bystate)

        unique_cargo_to_trucks = False
        truck_cargo_map = defaultdict(list)
        cargo_to_truck = []

        while not unique_cargo_to_trucks:
            unique_cargo_to_trucks = True
        
            for curr_cargo in self._cargo_list:
                truck, distance = truck_locator.find_nearest_truck(curr_cargo)
                truck_cargo_map[truck].append((curr_cargo, distance))

            for curr_truck in truck_cargo_map:
                if len(truck_cargo_map[curr_truck]) > 1:
                    self._remove_duplicates(curr_truck, truck_cargo_map)
                    
                    cargo, distance = self._get_cargo_distance(curr_truck, truck_cargo_map)

                    self._trucks_bystate[curr_truck.state].remove(curr_truck)
                    self._cargo_list.remove(cargo)
                    
                    cargo_to_truck.append((cargo, curr_truck, distance))

                    unique_cargo_to_trucks = False

        return cargo_to_truck

    def _remove_duplicates(self, truck, truck_cargo_map):
        """ Removes duplicates from the given truck to cargo mapping

            This function removes all cargos except for the one that is furthest away from the truck. The 
            farthest cargo from the truck is the best match for that given cargo in order to have a minimum 
            overall truck distance.

            Args:
                truck: Current Truck being processed.
                truck_cargo_map: Truck cargo dict being processed
        """
        furthest_cargo, furthest_distance = self._get_cargo_distance(truck, truck_cargo_map)
        
        for (curr_cargo, curr_distance) in truck_cargo_map[truck]:
            if curr_distance > furthest_distance:
                truck_cargo_map[truck].remove((furthest_cargo, furthest_distance))
                (furthest_cargo, furthest_distance) = (curr_cargo, curr_distance)
            else:
                truck_cargo_map[truck].remove((curr_cargo, curr_distance))

    def _get_cargo_distance(self, truck, truck_cargo_map):
        return truck_cargo_map[truck][0][0], truck_cargo_map[truck][0][1]