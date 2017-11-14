from core.truck import Truck
from core.cargo  import Cargo
from utils.us_states import NEIGHBOURS

class TruckLocator:
    def __init__(self, trucks_bystate):
        """Constructor for the TruckLocator class

        Attributes:
            trucks_bystate: Truck list sorte by state
        """
        self._trucks_bystate = trucks_bystate

    def find_nearest_truck(self, cargo):
        """ Finds the nearest truck to the given Cargo object

        Args:
            cargo: Cargo with coordinate information

        Returns:
            A tuple in which the first element is the nearest truck to that cargo and the second
            element is the distance in Km from the truck to the cargo.
            (Truck Object, Distance)
        """
        if len(self._trucks_bystate) == 0:
            return None, None

        self._cargo = cargo
        self._visited_states = set()

        return self._nearest_truck(self._cargo.origin_state)

    def _nearest_truck(self, origin_state):
        """Recursive function to look for trucks in origin and nearby states

        This function first searches for available trucks in the cargos origin state, it than looks for
        trucks in the neighbour states from the cargo state. If trucks are found, the function selects
        the closest truck as the chosen one, if no trucks are found in the origin and neighbour states,
        the function expands the search area and looks for trucks in the neighbour's neighbour states.

        Args:
            origin_state: Current state being checked for nearby trucks

        Returns:
            A tuple in which the first element is the nearest truck to that cargo and the second
            element is the distance in Km from the truck to the cargo.
            (Truck Object, Distance)    
        """
        nearest_truck_origin_state = None
        shortest_distance_origin_state = -1.
        nearest_truck_neighbours = None
        shortest_distance_neighbours = -1.

        if (len(self._trucks_bystate[origin_state]) > 0) and (origin_state not in self._visited_states) :
            nearest_truck_origin_state, shortest_distance_origin_state = self._nearest_truck_in_state(origin_state)
        
        self._visited_states.add(origin_state)

        self._search_area = NEIGHBOURS[origin_state]
        nearest_truck_neighbours, shortest_distance_neighbours = self._find_trucks_in_neighbours()

        if (shortest_distance_neighbours == -1.) and (shortest_distance_origin_state == -1.):            
            while shortest_distance_neighbours == -1.:
                self._expand_search_area()
                nearest_truck_neighbours, shortest_distance_neighbours = self._find_trucks_in_neighbours()

        if shortest_distance_origin_state == -1:
            return nearest_truck_neighbours, shortest_distance_neighbours
        elif shortest_distance_neighbours == -1:
            return nearest_truck_origin_state, shortest_distance_origin_state
        
        if shortest_distance_origin_state < shortest_distance_neighbours:
            return nearest_truck_origin_state, shortest_distance_origin_state
        else:
            return nearest_truck_neighbours, shortest_distance_neighbours


    def _nearest_truck_in_state(self, state):
        """Looks for the nearest truck relative to the given cargo

        Args:
            state: State to search for trucks

        Returns:
            A tuple in which the first element is the nearest truck to that cargo and the second
            element is the distance in Km from the truck to the cargo.
            (Truck Object, Distance)
        """
        nearest_truck = None
        shortest_distance = -1.
        state_truck_list = self._trucks_bystate[state]

        for curr_truck in state_truck_list:
            if shortest_distance == -1.:
                shortest_distance = curr_truck.location.distance_to(self._cargo.origin)
                nearest_truck = curr_truck
            else:
                distance = curr_truck.location.distance_to(self._cargo.origin)
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_truck = curr_truck

        return nearest_truck, shortest_distance

    def _find_trucks_in_neighbours(self):
        """Looks for trucks in the given origin_state neighbours

        Returns:
            A tuple in which the first element is the nearest truck to that cargo and the second
            element is the distance in Km from the truck to the cargo.
            (Truck Object, Distance)    
        """
        nearest_truck_neighbours = None
        shortest_distance_neighbours = -1.

        for curr_neighbour in self._search_area:
            if(curr_neighbour not in self._trucks_bystate):
                continue

            if (len(self._trucks_bystate[curr_neighbour]) == 0) and (curr_neighbour not in self._visited_states):
                self._visited_states.add(curr_neighbour)
                continue

            neighbour_truck, curr_distance = self._nearest_truck_in_state(curr_neighbour)
            
            if (curr_distance < shortest_distance_neighbours) or (shortest_distance_neighbours == -1.):
                nearest_truck_neighbours = neighbour_truck
                shortest_distance_neighbours = curr_distance

            self._visited_states.add(curr_neighbour)

        return nearest_truck_neighbours, shortest_distance_neighbours

    def _expand_search_area(self):
        expanded_search_area = []
        for curr_neighbour in self._search_area:
            for curr_neighbour_neighbour in NEIGHBOURS[curr_neighbour]:
                if curr_neighbour_neighbour not in self._visited_states:
                    expanded_search_area.append(curr_neighbour_neighbour)
        self._search_area = expanded_search_area