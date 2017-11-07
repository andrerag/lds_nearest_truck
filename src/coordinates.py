import math

class Coordinates:
	def __init__(self, lat, lng):
		self.lat = lat
		self.lng = lng
	
	def distance_to(coordinates):
		return harvesine_distance(coordinates)
	
	def haversine_distance(coordinates):
		earth_radius = 6371e3
		phi1 = math.radians(coordinates.lat)
		phi2 = math.radians(self.lat)		
		delta_phi = math.radians(coordinates.lat - self.lat)
		delta_lambda = math.radians(coordinates.lng - self.lng)
		
		a = math.sin(delta_phi/2) * math.sin(delta_phi/2) +
			math.cos(phi1) * math.cos(phi2) *
			math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
			
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		
		return (earth_radius * c)	