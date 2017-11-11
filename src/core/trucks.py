from core.coordinates import Coordinates

class Truck:
	def __init__(self, truck, city, state, lat, lng):
		self.truck = truck
		self.city  = city
		self.state = state
		self.location = Coordinates(lat, lng)

	def __hash__(self):
		return hash(self.truck)

	def __eq__(self, other):
		return self.truck == other.truck