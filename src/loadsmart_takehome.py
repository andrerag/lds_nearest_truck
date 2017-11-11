import logging
from optparse import OptionParser

from core import cargo_truck_mapper as mapper
from utils import csv_parser
from plotter import map_plotter

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
	
	truck_list = csv_parser.load_trucks_bystate(options.trucks_csvfile)
	cargo_list = csv_parser.load_cargo_list(options.cargos_csvfile)
	truck_cargo_mapping, distance = mapper.map_cargos_to_trucks(cargo_list, truck_list)

	map_plotter.plot_results(cargo_list, truck_list, truck_cargo_mapping)