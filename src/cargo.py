from coordinates import Coordinates

class Cargo:
	def __init__(self, product,origin_city,origin_state,origin_lat,origin_lng,
				 destination_city,destination_state,destination_lat,destination_lng):
		self.product           		 = product		
		self.origin_city       		 = origin_city
		self.origin_state      		 = origin_state
		self.origin	 	 			 = Coordinates(origin_lat, origin_lng)		
		self.destination_city  		 = destination_city
		self.destination_state 		 = destination_state
		self.destination		     = Coordinates(destination_lat, destination_lng)
