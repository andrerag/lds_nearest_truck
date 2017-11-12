import gmplot

from utils import csv_parser
from core.trucks import Truck
from core.cargo import Cargo

def plot_results(cargos_csvfile, trucks_csvfile, truck_cargo_mapping):
	truck_list = csv_parser.load_trucks_bystate(trucks_csvfile)
	cargo_list = csv_parser.load_cargo_list(cargos_csvfile)

	CARGO = 0

	gmap = gmplot.GoogleMapPlotter.from_geocode('United States', 5)

	for truck in truck_cargo_mapping:
		path = [(truck_cargo_mapping[truck][0][CARGO].origin.lat, truck.location.lat), 
			(truck_cargo_mapping[truck][0][CARGO].origin.lng, truck.location.lng)]
		gmap.plot(path[0], path[1], "black", edge_width=2)

	for cargo in cargo_list:
		gmap.marker(cargo.origin.lat, cargo.origin.lng, 'red')

	for state in truck_list:
		for curr_truck in truck_list[state]:
			gmap.marker(curr_truck.location.lat, curr_truck.location.lng, 'yellow')
	
	gmap.draw("results.html")