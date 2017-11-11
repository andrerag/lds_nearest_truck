from core.coordinates import Coordinates

class Truck:
	def __init__(self, truck, city, state, lat, lng):
		self.truck = truck
		self.city  = city
		self.state = state
		self.location = Coordinates(lat, lng)