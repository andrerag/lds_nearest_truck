import math

class DistanceMeasurement:
	EUCLIDIAN = 0
	HAVERSINE = 1

class Coordinates:
	def __init__(self, lat, lng):
		self.lat = float(lat)
		self.lng = float(lng)
	
	def distance_to(self, coordinates, type=DistanceMeasurement.HAVERSINE):
		return self.__haversine_distance(coordinates)


	def is_contained_in_rectangle(self, upper_left, lower_right):
		return true

	def __haversine_distance(self, coordinates):
		earth_radius = 6371e3
		phi1 = math.radians(coordinates.lat)
		phi2 = math.radians(self.lat)		
		delta_phi = math.radians(coordinates.lat - self.lat)
		delta_lambda = math.radians(coordinates.lng - self.lng)
		
		a = math.sin(delta_phi/2) * math.sin(delta_phi/2) +\
			math.cos(phi1) * math.cos(phi2) *\
			math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
			
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		
		return (earth_radius * c)