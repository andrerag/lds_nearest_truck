import gmplot

from core.trucks import Truck
from core.cargo import Cargo

def plot_results(cargos, truck_list_bystate, truck_cargo_mapping):
	TRUCK = 0
	CARGO = 1

	gmap = gmplot.GoogleMapPlotter.from_geocode('United States', 5)

	for truck_cargo in truck_cargo_mapping:
		path = [(truck_cargo[CARGO].origin.lat, truck_cargo[TRUCK].location.lat), \
			(truck_cargo[CARGO].origin.lng, truck_cargo[TRUCK].location.lng)]
		gmap.plot(path[TRUCK], path[CARGO], "black", edge_width=2)

	for cargo in cargos:
		gmap.marker(cargo.origin.lat, cargo.origin.lng, 'red')

	for state in truck_list_bystate:
		for curr_truck in truck_list_bystate[state]:
			gmap.marker(curr_truck.location.lat, curr_truck.location.lng, 'yellow')
	
	gmap.draw("results.html")