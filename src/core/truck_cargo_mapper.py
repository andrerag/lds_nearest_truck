from core import truck_locator

from core.trucks import Truck
from core.cargo  import Cargo

def map_cargos_to_trucks(cargo_list, trucks_bystate):
	truck_cargo_mapping = []
	total_distance = 0.

	for curr_cargo in cargo_list:
		truck, distance = truck_locator.find_nearest_truck(curr_cargo, trucks_bystate)
		truck_cargo_mapping.append((truck, curr_cargo))
		total_distance += distance

	return truck_cargo_mapping, total_distance