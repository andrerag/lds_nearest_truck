import math

class DistanceMeasurement:
	EUCLIDIAN = 0
	HAVERSINE = 1

class Coordinates:
	def __init__(self, lat, lng):
		self.lat = float(lat)
		self.lng = float(lng)
	
	def distance_to(self, coordinates, type=DistanceMeasurement.HAVERSINE):
		if type == DistanceMeasurement.HAVERSINE:
			return self.__haversine_distance(coordinates)

	def __haversine_distance(self, coordinates):
		earth_radius = float(6371e3)
		phi1 = math.radians(coordinates.lat)
		phi2 = math.radians(self.lat)		
		delta_phi = math.radians(coordinates.lat - self.lat)
		delta_lambda = math.radians(coordinates.lng - self.lng)
		
		halfchord_square = math.sin(delta_phi/2) * math.sin(delta_phi/2) +\
						   math.cos(phi1) * math.cos(phi2) *\
						   math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
			
		angular_distance = 2 * math.atan2(math.sqrt(halfchord_square), math.sqrt(1 - halfchord_square))
		
		return (earth_radius * angular_distance)