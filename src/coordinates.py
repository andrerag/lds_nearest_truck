import math

class DistanceMeasurement:
	EUCLIDIAN = 0
	HAVERSINE = 1

class Coordinates:
	def __init__(self, lat, lng):
		self.lat = lat
		self.lng = lng
	
	def distance_to(coordinates, type=DistanceMeasurement.HAVERSINE):
		if (type == DistanceMeasurement.HAVERSINE):
			return __harvesine_distance(coordinates)

		return -1

	def is_contained_in_rectangle(upper_left, lower_right):
		return true

	def __haversine_distance(coordinates):
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