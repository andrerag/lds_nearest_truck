import csv

from collections import defaultdict
from core.trucks import Truck
from core.cargo  import Cargo

def load_trucks_bystate(csvfile):
    """Reads a .csv file and returns a truck list sorted by state
    
    This function takes a csv file as input with the following columns: truck, city, state, lat, lng

    Args:
        csvfile: .csv file containing truck info

    Returns:
        A dict object with the folowing format:
        {'State': (Truck1, Truck2, Truck3...)}

    """
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
    """Reads a .csv file and returns a Cargo object list

    This function takes a csv file as input with the following columns: product, origin_city, 
    origin_state, origin_lat, origin_lng, destination_city, destination_state, destination_lat,
    destination_lng

    Args:
        csvfile: .csv file containing cargo info

    Returns:
        A list of Cargo objects

    """
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