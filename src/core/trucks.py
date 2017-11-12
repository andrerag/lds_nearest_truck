from core.coordinates import Coordinates
from utils.neighbour_states import NEIGHBOURS
from utils.neighbour_states import InvalidUSState

class Truck(object):
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
		self._state = state
		self.location = Coordinates(lat, lng)

	def __hash__(self):
		"""Hash function so the Truck class can be used as a dictionary key"""
		return hash(self.truck)

	def __eq__(self, other):
		return self.truck == other.truck

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, value):
		"""Setter method for the US state info

		Args:
			value: Valid US State

		Raises:
			InvalidUSState: The state given does not belog to the US
		"""
		if value not in NEIGHBOURS:
			raise InvalidUSState("Given state does not belong to the United States")
		self._state = value
