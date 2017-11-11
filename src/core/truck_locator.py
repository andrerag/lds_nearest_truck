from core.trucks import Truck
from core.cargo  import Cargo
from utils.neighbour_states import NEIGHBOURS

def find_nearest_truck(cargo, trucks_bystate):
	if len(trucks_bystate) == 0:
		return None, None

	visited_states = set()
	return nearest_truck(cargo.origin_state, cargo, trucks_bystate, visited_states)

def nearest_truck(root_state ,cargo, trucks_bystate, visited_states):
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

	# If no trucks were found, recursevly look for trucks in the neighbour's neighbours

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
	nearest_truck = ''
	shortest_distance = -1.0

	for curr_truck in state_truck_list:
		if shortest_distance == -1.0:
			shortest_distance = curr_truck.location.distance_to(cargo.origin)
			nearest_truck = curr_truck
		else:
			distance = curr_truck.location.distance_to(cargo.origin)
			if distance < shortest_distance:
				shortest_distance = distance
				nearest_truck = curr_truck

	return nearest_truck, shortest_distance

def find_trucks_in_neighbours(root_state ,cargo, trucks_bystate, visited_states):
	nearest_truck_neighbours = ''
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