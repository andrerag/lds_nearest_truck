import csv

from collections import defaultdict
from trucks import Truck
from cargo import Cargo

def load_trucks_bystate(csvfile):
	truck_list_bystate = defaultdict(list)
	with open(csvfile) as trucks_csvfile:
		reader = csv.DictReader(trucks_csvfile)
		for curr_truck in reader:
			new_truck = Truck(curr_truck['truck'],\
				  			  curr_truck['city'],\
							  curr_truck['state'],\
							  curr_truck['lat'],\
							  curr_truck['lng'])
			truck_list_bystate[curr_truck['state']].append(new_truck)
	return truck_list_bystate

def load_cargo_list(csvfile):
	cargo_list = []
	with open(csvfile) as cargo_csvfile:
		reader = csv.DictReader(cargo_csvfile)
		for curr_cargo in reader:
			cargo_list.append(Cargo(curr_cargo['product'],\
									curr_cargo['origin_city'],\
									curr_cargo['origin_state'],\
									curr_cargo['origin_lat'],\
									curr_cargo['origin_lng'],\
									curr_cargo['destination_city'],\
									curr_cargo['destination_state'],\
									curr_cargo['destination_lat'],\
									curr_cargo['destination_lng']))
	return cargo_list