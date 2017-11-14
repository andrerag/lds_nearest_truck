import unittest
from collections import defaultdict

from core.truck import Truck
from core.truck_locator import TruckLocator
from core.cargo import Cargo

class TruckLocatorTest(unittest.TestCase):
    def setUp(self):
        self.cargo = Cargo('Pandeiro', 'Fremont', 'WY', 42.870041, -107.744649,
                      'Boston', 'MA', 42.365167, -71.084856)

    def test_trucks_in_state(self):
        truck1 = Truck('RecifeTransport', 'County1', 'WY', 44.650855, -104.687268) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'WY', 44.022229, -105.478284) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'WY', 43.562262, -106.071546) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'WY', 42.825402, -107.631604) #Really close
        
        trucks_bystate = {'WY': [truck1]}

        locator = TruckLocator(trucks_bystate)

        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck1)

        trucks_bystate['WY'].append(truck2)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck2)
        trucks_bystate['WY'].append(truck3)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck3)
        trucks_bystate['WY'].append(truck4)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)
		
    def test_trucks_in_state_alltaonce(self):
        truck1 = Truck('RecifeTransport', 'County1', 'WY', 44.650855, -104.687268) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'WY', 44.022229, -105.478284) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'WY', 43.562262, -106.071546) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'WY', 42.825402, -107.631604) #Really close
        
        trucks_bystate = defaultdict(list)
        trucks_bystate['WY'].append(truck1)
        trucks_bystate['WY'].append(truck2)
        trucks_bystate['WY'].append(truck3)
        trucks_bystate['WY'].append(truck4)

        locator = TruckLocator(trucks_bystate)

        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)    

    def test_trucks_in_state_and_neighbours(self):
        truck1 = Truck('RecifeTransport', 'County1', 'WY', 44.650855, -104.687268) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'WY', 44.022229, -105.478284) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'WY', 43.562262, -106.071546) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'WY', 42.825402, -107.631604) #Really close

        truck5 = Truck('RecifeTransport', 'County5', 'MT', 47.766819, -107.983167) #Other State
        truck6 = Truck('RecifeTransport', 'County5', 'MT', 45.642636, -107.939221) #Other State
        
        trucks_bystate = defaultdict(list)
        locator = TruckLocator(trucks_bystate)
        
        trucks_bystate['WY'].append(truck1)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck1)
        trucks_bystate['WY'].append(truck2)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck2)
        trucks_bystate['WY'].append(truck3)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck3)
        trucks_bystate['WY'].append(truck4)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)
        
        trucks_bystate['MT'].append(truck5)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)
        trucks_bystate['MT'].append(truck6)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)
    
    def test_trucks_in_state_and_neighbours_alltaonce(self):
        truck1 = Truck('RecifeTransport', 'County1', 'WY', 44.650855, -104.687268) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'WY', 44.022229, -105.478284) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'WY', 43.562262, -106.071546) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'WY', 42.825402, -107.631604) #Really close
        truck5 = Truck('RecifeTransport', 'County5', 'MT', 47.766819, -107.983167) #Other State
        truck6 = Truck('RecifeTransport', 'County5', 'MT', 45.642636, -107.939221) #Other State
        
        trucks_bystate = defaultdict(list)
        
        trucks_bystate['WY'].append(truck1)
        trucks_bystate['WY'].append(truck2)
        trucks_bystate['WY'].append(truck3)
        trucks_bystate['WY'].append(truck4)        
        trucks_bystate['MT'].append(truck5)
        trucks_bystate['MT'].append(truck6)
        
        locator = TruckLocator(trucks_bystate)       
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)    

    def test_trucks_only_other_states(self):
        truck1 = Truck('RecifeTransport', 'County1', 'MT', 48.208000, -115.365980) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'MT', 47.440887, -105.566175) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'SD', 44.384512, -99.523694) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'NE', 41.769037, -101.633069) #Really close
        truck5 = Truck('RecifeTransport', 'County4', 'CO', 40.911208, -107.214124) #Really close

        trucks_bystate = defaultdict(list)
        locator = TruckLocator(trucks_bystate)

        trucks_bystate['MT'].append(truck1)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck1)
        trucks_bystate['MT'].append(truck2)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck2)
        trucks_bystate['SD'].append(truck3)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck3)
        trucks_bystate['NE'].append(truck4)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck4)
        trucks_bystate['CO'].append(truck5)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck5)
        
    def test_trucks_only_other_states_alltaonce(self):
        truck1 = Truck('RecifeTransport', 'County1', 'MT', 48.208000, -115.365980) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'MT', 47.440887, -105.566175) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'SD', 44.384512, -99.523694) #Close
        truck4 = Truck('RecifeTransport', 'County4', 'NE', 41.769037, -101.633069) #Really close
        truck5 = Truck('RecifeTransport', 'County4', 'CO', 40.911208, -107.214124) #Really close

        trucks_bystate = defaultdict(list)

        trucks_bystate['MT'].append(truck1)
        trucks_bystate['MT'].append(truck2)
        trucks_bystate['SD'].append(truck3)
        trucks_bystate['NE'].append(truck4)
        trucks_bystate['CO'].append(truck5)
        
        locator = TruckLocator(trucks_bystate)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck5)    
        

    def test_trucks_in_neighbours_neighbour(self):
        truck1 = Truck('RecifeTransport', 'County1', 'NM', 32.932369, -106.005628) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'AZ', 36.789248, -109.257581) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'KS', 39.748937, -101.661409) #Close

        trucks_bystate = defaultdict(list)
        locator = TruckLocator(trucks_bystate)

        trucks_bystate['NM'].append(truck1)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck1)
        trucks_bystate['AZ'].append(truck2)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck2)
        trucks_bystate['KS'].append(truck3)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck3)

    def test_trucks_in_neighbours_neighbour_alltaonce(self):
        truck1 = Truck('RecifeTransport', 'County1', 'NM', 32.932369, -106.005628) #Farthest
        truck2 = Truck('RecifeTransport', 'County2', 'AZ', 36.789248, -109.257581) #Near
        truck3 = Truck('RecifeTransport', 'County3', 'KS', 39.748937, -101.661409) #Close

        trucks_bystate = defaultdict(list)

        trucks_bystate['NM'].append(truck1)
        trucks_bystate['AZ'].append(truck2)
        trucks_bystate['KS'].append(truck3)
        
        locator = TruckLocator(trucks_bystate)
        self.assertEqual(locator.find_nearest_truck(self.cargo)[0], truck3)
