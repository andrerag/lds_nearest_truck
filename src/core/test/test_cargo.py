import unittest

from utils.us_states import NEIGHBOURS
from utils.us_states import InvalidUSState
from core.cargo import Cargo

class CargoTest(unittest.TestCase):
    def test_create_valid_cargo(self):
        for us_state in NEIGHBOURS:
            valid_cargo = Cargo('Maracatu', 'Recife', us_state, -90., -90.,
                                'Campina Grande', us_state, -90., -90.,)
            self.assertEqual(valid_cargo.product, 'Maracatu')
            self.assertEqual(valid_cargo.origin_city, 'Recife')
            self.assertEqual(valid_cargo.origin_state, us_state)
            self.assertEqual(valid_cargo.origin.lat, -90.)
            self.assertEqual(valid_cargo.origin.lng, -90.)
            self.assertEqual(valid_cargo.destination_city, 'Campina Grande')
            self.assertEqual(valid_cargo.destination_state, us_state)
            self.assertEqual(valid_cargo.destination.lat, -90.)
            self.assertEqual(valid_cargo.destination.lng, -90.)
    
    def test_create_invalid_cargo(self):
        with self.assertRaises(InvalidUSState):
            invalid_cargo = Cargo('Maracatu', 'Recife', 'PE', -90., -90.,
                                  'Campina Grande', 'MO', -90., -90.,)
        with self.assertRaises(InvalidUSState):
            invalid_cargo = Cargo('Maracatu', 'Recife', 'MO', -90., -90.,
                                  'Campina Grande', 'PB', -90., -90.,)
