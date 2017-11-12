from core.trucks import Truck
from core.cargo  import Cargo
from utils.neighbour_states import NEIGHBOURS

def find_nearest_truck(cargo, trucks_bystate):
	""" Finds the nearest truck to the given Cargo object

		Args:
			cargo: Cargo with coordinate information
			trucks_bystate: Truck list sorted by the US state they are located

		Returns:
			A tuple in which the first element is the nearest truck to that cargo and the second
			element is the distance in Km from the truck to the cargo.
			(Truck Object, Distance)
	"""
	if len(trucks_bystate) == 0:
		return None, None

	visited_states = set()
	return nearest_truck(cargo.origin_state, cargo, trucks_bystate, visited_states)

def nearest_truck(root_state ,cargo, trucks_bystate, visited_states):
	"""Recursive function to look for trucks in origin and nearby states

	This function first searches for available trucks in the cargos origin state, it than looks for
	trucks in the neighbour states from the cargo state. If trucks are found, the function selects
	the closest truck as the chosen one, if no trucks are found in the origin and neighbour states,
	the function is recursevly called to look for trucks in the neighbour's neighbour states.
	Currently the function makes a copy of the cargo and truck list so it doensn't affect the 
	referrences given, but it's not very space efficient.

	Args:
		root_state: Current state being checked for nearby trucks
		cargo: Cargo object conatining lattitude and longitude information
		trucks_bystate: Truck list sorte by the state they are located
		visited_states: List of states that have been checked for trucks

	Returns:
		A tuple in which the first element is the nearest truck to that cargo and the second
		element is the distance in Km from the truck to the cargo.
		(Truck Object, Distance)	
	"""
	nearest_truck_root_state = None
	shortest_distance_root_state = -1.
	nearest_truck_neighbours = None
	shortest_distance_neighbours = -1.

	if (len(trucks_bystate[root_state]) > 0) and (root_state not in visited_states) :
		nearest_truck_root_state, shortest_distance_root_state = nearest_truck_in_state(cargo, 
			trucks_bystate[root_state])
	
	visited_states.add(root_state)

	nearest_truck_neighbours, shortest_distance_neighbours = find_trucks_in_neighbours(root_state, 
		cargo, trucks_bystate, visited_states)

	if (shortest_distance_neighbours == -1.) and (shortest_distance == -1.):
		for curr_neighbour in NEIGHBOURS[cargo.origin_state]:
			nearest_truck_root_state, shortest_distance_root_state = nearest_truck(curr_neighbour, 
				cargo, trucks_bystate, visited_states)

	if shortest_distance_root_state == -1:
		return nearest_truck_neighbours, shortest_distance_neighbours
	elif shortest_distance_neighbours == -1:
		return nearest_truck_root_state, shortest_distance_root_state
	
	if shortest_distance_root_state < shortest_distance_neighbours:
		return nearest_truck_root_state, shortest_distance_root_state
	else:
		return nearest_truck_neighbours, shortest_distance_neighbours


def nearest_truck_in_state(cargo, state_truck_list):
	"""Looks for the nearest truck relative to the given cargo

	Args:
		cargo: Cargo object conatining lattitude and longitude information
		state_truck_list: List of trucks located in a given state.

	Returns:
		A tuple in which the first element is the nearest truck to that cargo and the second
		element is the distance in Km from the truck to the cargo.
		(Truck Object, Distance)
	"""
	nearest_truck = None
	shortest_distance = -1.

	for curr_truck in state_truck_list:
		if shortest_distance == -1.:
			shortest_distance = curr_truck.location.distance_to(cargo.origin)
			nearest_truck = curr_truck
		else:
			distance = curr_truck.location.distance_to(cargo.origin)
			if distance < shortest_distance:
				shortest_distance = distance
				nearest_truck = curr_truck

	return nearest_truck, shortest_distance

def find_trucks_in_neighbours(root_state ,cargo, trucks_bystate, visited_states):
	"""Looks for trucks in the given root_state neighbours

	Args:
		root_state: Current state being checked for nearby trucks
		cargo: Cargo object conatining lattitude and longitude information
		trucks_bystate: Truck list sorted by the US state they are located
		visited_states: List of states that have been checked for trucks

	Returns:
		A tuple in which the first element is the nearest truck to that cargo and the second
		element is the distance in Km from the truck to the cargo.
		(Truck Object, Distance)	
	"""
	nearest_truck_neighbours = None
	shortest_distance_neighbours = -1.

	for curr_neighbour in NEIGHBOURS[root_state]:
		if (len(trucks_bystate[curr_neighbour]) == 0) and (curr_neighbour not in visited_states):
			visited_states.add(curr_neighbour)
			continue

		neighbour_truck, curr_distance = nearest_truck_in_state(cargo, trucks_bystate[curr_neighbour])
		if (curr_distance < shortest_distance_neighbours) or (shortest_distance_neighbours is -1.):
			nearest_truck_neighbours = neighbour_truck
			shortest_distance_neighbours = curr_distance

		visited_states.add(curr_neighbour)

	return 	nearest_truck_neighbours, shortest_distance_neighbours