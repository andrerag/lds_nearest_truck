import unittest

from utils.us_states import NEIGHBOURS
from utils.us_states import InvalidUSState
from core.trucks import Truck

class TruckTest(unittest.TestCase):
    def test_create_valid_truck(self):
        for us_state in NEIGHBOURS:
            valid_truck = Truck('Maracatu', 'Recife', us_state, -90., -90.)
            self.assertEqual(valid_truck.truck, 'Maracatu')
            self.assertEqual(valid_truck.city, 'Recife')
            self.assertEqual(valid_truck.state, us_state)
            self.assertEqual(valid_truck.location.lat, -90.)
            self.assertEqual(valid_truck.location.lng, -90.)

    def test_create_invalid_truck(self):
        with self.assertRaises(InvalidUSState):
            invalid_truck = Truck('Maracatu', 'Recife', 'PE', -90., -90.)
        with self.assertRaises(InvalidUSState):
            invalid_truck = Truck('Maracatu', 'Recife', 'MO', -90., -90.)
