from core.coordinates import Coordinates

class Truck:
	""" This class represents a single Truck. It contains truck description and it's location

	    Attributes:
	        truck: Truck description
	        city: City where the truck is located
	        state: State where the truck is located
	        location: Coordinates object containing latitude and longitude
	"""
	def __init__(self, truck, city, state, lat, lng):
		"""Constructor for the Truck class"""
		self.truck = truck
		self.city  = city
		self.state = state
		self.location = Coordinates(lat, lng)

	def __hash__(self):
		"""Hash function so the Truck class can be used as a dictionary key"""
		return hash(self.truck)

	def __eq__(self, other):
		return self.truck == other.truck