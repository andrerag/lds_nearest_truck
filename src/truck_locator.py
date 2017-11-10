from cargo import Cargo
from trucks import Truck

def find_nearest_truck(cargo, trucks_bystate):
	shortest_distance = -1.0
	nearest_truck = ''

	for curr_truck in trucks_bystate[cargo.origin_state]:
		if shortest_distance == -1.0:
			shortest_distance = curr_truck.location.distance_to(cargo.origin)
			nearest_truck = curr_truck
		else:
			distance = curr_truck.location.distance_to(cargo.origin)
			if distance < shortest_distance:
				shortest_distance = distance
				nearest_truck = curr_truck

	return (nearest_truck, shortest_distance)

