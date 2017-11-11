import logging
import gmplot
import truck_locator

from optparse import OptionParser
from csv_parser import *

if __name__ == "__main__":
	usage = "usage: %prog --trucks=<CSVFILE> --cargo=<CSVFILE>"
	cmd_args_parser = OptionParser(usage=usage)
	cmd_args_parser.add_option("--trucks", dest="trucks_csvfile", 
							   help=".csv File containing trucks locations")
	cmd_args_parser.add_option("--cargos", dest="cargos_csvfile", 
							   help=".csv File containing cargo locations and destination")
	
	(options, args) = cmd_args_parser.parse_args()
	if not(options.trucks_csvfile) or not(options.cargos_csvfile):
		cmd_args_parser.error("No .csv file contanning truck or cargo location was given.")
	
	logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
	
	truck_list = load_trucks_bystate(options.trucks_csvfile)
	cargo_list = load_cargo_list(options.cargos_csvfile)

	truck, distance = truck_locator.find_nearest_truck(cargo_list[0], truck_list)

	print truck.city, truck.state

