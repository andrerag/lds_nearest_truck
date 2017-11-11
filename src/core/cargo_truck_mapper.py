from copy import deepcopy
from collections import defaultdict

from core import truck_locator
from core.trucks import Truck
from core.cargo  import Cargo

def map_cargos_to_trucks(cargo_list, trucks_bystate):
	unique_cargo_to_trucks = False
	trucks_bystate_cpy = deepcopy(trucks_bystate)
	cargo_list_cpy = deepcopy(cargo_list)

	cargo_truck_map = defaultdict(list)

	while not unique_cargo_to_trucks:
		unique_cargo_to_trucks = True
	
		for curr_cargo in cargo_list_cpy:
			truck, distance = truck_locator.find_nearest_truck(curr_cargo, trucks_bystate_cpy)
			cargo_truck_map[truck].append((curr_cargo, distance))

		for curr_truck in cargo_truck_map:
			if len(cargo_truck_map[curr_truck]) > 1:
				remove_duplicates(curr_truck, cargo_truck_map, trucks_bystate_cpy)
				
				trucks_bystate_cpy[curr_truck.state].remove(curr_truck)
				cargo_list_cpy.remove(cargo_truck_map[curr_truck][0][0])

				unique_cargo_to_trucks = False

	return	cargo_truck_map, get_total_distance(cargo_truck_map)

def remove_duplicates(truck, cargo_truck_map, trucks_bystate):
	(furthest_cargo, furthest_distance) = cargo_truck_map[truck][0]
	
	for (curr_cargo, curr_distance) in cargo_truck_map[truck]:
		if curr_distance > furthest_distance:
			cargo_truck_map[truck].remove((furthest_cargo, furthest_distance))
			(furthest_cargo, furthest_distance) = (curr_cargo, curr_distance)
		else:
			cargo_truck_map[truck].remove((curr_cargo, curr_distance))

def get_total_distance(cargo_truck_map):
	return 0;