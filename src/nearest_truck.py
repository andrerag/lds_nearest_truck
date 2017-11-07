import logging
import gmplot

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
	
	logging.info('Parsing trucks .csv file')
	truck_list = load_truck_list(options.trucks_csvfile)
	logging.info('Parsing cargos .csv file')
	cargo_list = load_cargo_list(options.cargos_csvfile)

	a = truck_list[0].location.distance_to(cargo_list[0].origin)
	logging.info('Distance from [%s, %s] to [%s, %s]: %d', truck_list[0].city, truck_list[0].state, \
		cargo_list[0].origin_city, cargo_list[0].origin_state, a)