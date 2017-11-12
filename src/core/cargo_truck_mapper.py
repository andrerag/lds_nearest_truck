from copy import deepcopy
from collections import defaultdict

from core import truck_locator
from core.trucks import Truck
from core.cargo  import Cargo

def map_cargos_to_trucks(cargo_list, trucks_bystate):
	"""Maps cargos to trucks

	This fuction goes through the cargo list and finds the appropriate truck for it. The appropriate
	truck for a given cargo is the nearest truck possible in a way that it assures that the distance
	travelled by all trucks is the minimum possible. This function also checks if a truck was
	assigned to more than one cargo, if that happens, the function calls remove_duplicates() in
	order to fix the issue. Currently the function makes a copy of the cargo and truck list so it 
	doensn't affect the referrences given, but it's not very space efficient.

	Args:
		cargo_list: The list of cargos to find the nearest truck
		trucks_bystate: Dictionary object of all trucks sorted by the state they are located

	Returns:
		A dict mapping of the trucks and their respective cargos. Currently the dict has the
		following structure:

		{'Truck Object': ((Cargo Object, Distance to Truck))}

		Note that the value of the dict is a list of tuples. This needs to be corrected 

	"""
	unique_cargo_to_trucks = False
	trucks_bystate_cpy = deepcopy(trucks_bystate)
	cargo_list_cpy = deepcopy(cargo_list)

	truck_cargo_map = defaultdict(list)

	while not unique_cargo_to_trucks:
		unique_cargo_to_trucks = True
	
		for curr_cargo in cargo_list_cpy:
			truck, distance = truck_locator.find_nearest_truck(curr_cargo, trucks_bystate_cpy)
			truck_cargo_map[truck].append((curr_cargo, distance))

		for curr_truck in truck_cargo_map:
			if len(truck_cargo_map[curr_truck]) > 1:
				remove_duplicates(curr_truck, truck_cargo_map, trucks_bystate_cpy)
				
				trucks_bystate_cpy[curr_truck.state].remove(curr_truck)
				cargo_list_cpy.remove(truck_cargo_map[curr_truck][0][0])

				unique_cargo_to_trucks = False

	return	truck_cargo_map, get_total_distance(truck_cargo_map)

def remove_duplicates(truck, truck_cargo_map, trucks_bystate):
	""" Removes duplicates from the given truck to cargo mapping

		This function removes all cargos except for the one that is furthest away from the truck. The 
		farthest cargo from the truck is the best match for that given cargo in order to have a minimum 
		overall truck distance.

		Args:
			truck: Current Truck being processed.
			truck_cargo_map: Truck cargo dict being processed
			trucks_bystate: Truck list sorted by the states they are currently located

	"""
	(furthest_cargo, furthest_distance) = truck_cargo_map[truck][0]
	
	for (curr_cargo, curr_distance) in truck_cargo_map[truck]:
		if curr_distance > furthest_distance:
			truck_cargo_map[truck].remove((furthest_cargo, furthest_distance))
			(furthest_cargo, furthest_distance) = (curr_cargo, curr_distance)
		else:
			truck_cargo_map[truck].remove((curr_cargo, curr_distance))

def get_total_distance(truck_cargo_map):
	""" Returns the total distance that all trucks will travel

		Args:
			truck_cargo_map: Truck to Cargo dictionary
	"""
	return 0;