from collections import defaultdict

from core.truck_locator import TruckLocator
from core.trucks import Truck
from core.cargo  import Cargo

def map_cargos_to_trucks(cargo_list, trucks_bystate):
	"""Maps cargos to trucks

	This fuction goes through the cargo list and finds the appropriate truck for it. The appropriate
	truck for a given cargo is the nearest truck possible in a way that it assures that the distance
	travelled by all trucks is the minimum possible. This function also checks if a truck was
	assigned to more than one cargo, if that happens, the function calls remove_duplicates() in
	order to fix the issue.

	Args:
		cargo_list: The list of cargos to find the nearest truck
		trucks_bystate: Dictionary object of all trucks sorted by the state they are located

	Returns:
		A list tuple of the cargos and their respective trucks. Currently the list has the
		following structure:

		[(Cargo Object, Truck Object, Distance to Truck)]
	"""
	truck_locator = TruckLocator(trucks_bystate)

	unique_cargo_to_trucks = False
	truck_cargo_map = defaultdict(list)
	cargo_to_truck = []

	while not unique_cargo_to_trucks:
		unique_cargo_to_trucks = True
	
		for curr_cargo in cargo_list:
			truck, distance = truck_locator.find_nearest_truck(curr_cargo)
			truck_cargo_map[truck].append((curr_cargo, distance))

		for curr_truck in truck_cargo_map:
			if len(truck_cargo_map[curr_truck]) > 1:
				remove_duplicates(curr_truck, truck_cargo_map, trucks_bystate)
				
				trucks_bystate[curr_truck.state].remove(curr_truck)
				cargo_list.remove(truck_cargo_map[curr_truck][0][0])
				
				cargo_to_truck.append((truck_cargo_map[curr_truck][0][0], curr_truck, 
					truck_cargo_map[curr_truck][0][1]))

				unique_cargo_to_trucks = False

	return	cargo_to_truck

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