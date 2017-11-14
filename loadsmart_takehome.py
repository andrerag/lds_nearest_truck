import logging
from optparse import OptionParser

from core.cargo_truck_mapper import CargoTruckMapper
from utils import csv_parser

if __name__ == "__main__":
    usage = "usage: %prog --trucks=<CSVFILE> --cargo=<CSVFILE> --output=csv|html"
    cmd_args_parser = OptionParser(usage=usage)
    cmd_args_parser.add_option("--trucks", dest="trucks_csvfile", 
                               help=".csv File containing trucks locations")
    cmd_args_parser.add_option("--cargos", dest="cargos_csvfile", 
                               help=".csv File containing cargo locations and destination")
    cmd_args_parser.add_option("--output", dest="output_type", 
                               help="Choose 'csv' or 'html' to have a visual result using Google Maps")
    
    (options, args) = cmd_args_parser.parse_args()
    if not(options.trucks_csvfile) or not(options.cargos_csvfile):
        cmd_args_parser.error("No .csv file contanning truck or cargo location was given.")
        
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    
    logging.info("Parsing .csv files")
    truck_list = csv_parser.load_trucks_bystate(options.trucks_csvfile)
    cargo_list = csv_parser.load_cargo_list(options.cargos_csvfile)
    
    logging.info("Mapping cargo to trucks")
    mapper = CargoTruckMapper(cargo_list, truck_list)
    cargo_truck_mapping = mapper.map_cargos_to_trucks()

    if (not (options.output_type)) or (options.output_type == 'csv'):
        logging.info("Writing results to results.csv")
        csv_parser.generate_csv_results('results.csv', cargo_truck_mapping)
    elif options.output_type == 'html':
        from plotter import map_plotter
        logging.info("Plotting results to results.html")
        map_plotter.plot_results(options.cargos_csvfile, options.trucks_csvfile, cargo_truck_mapping)
    else:
        logging.info("Writing results to results.csv")
        csv_parser.generate_csv_results('results.csv', cargo_truck_mapping)    
