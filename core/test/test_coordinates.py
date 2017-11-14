import unittest
from core.coordinates import Coordinates
from core.coordinates import InvalidCoordinate

class CoordinatesTest(unittest.TestCase):
        def test_create_coordinate(self):
            coord_str  = Coordinates('34.79981', '-87.677251')
            coord_numb = Coordinates(34.79981, -87.677251)
            
            self.assertEqual(coord_str.lat, 34.79981)
            self.assertEqual(coord_str.lng, -87.677251)
            self.assertEqual(coord_numb.lat, 34.79981)
            self.assertEqual(coord_numb.lng, -87.677251)
            
        def test_invalid_lattitude(self):
            with self.assertRaises(InvalidCoordinate):
                coord = Coordinates(-91.0, -30.0)
            with self.assertRaises(InvalidCoordinate):
                coord1 = Coordinates(91.0, -30.0)
            with self.assertRaises(ValueErrorError):
                coord2 = Coordinates('not a number', -40.)
                
        def test_invalid_longitude(self):
            with self.assertRaises(InvalidCoordinate):
                coord = Coordinates(-34.0, -181.0)
            with self.assertRaises(InvalidCoordinate):
                coord1 = Coordinates(-34.0, 181.0)
            with self.assertRaises(ValueError):
                coord2 = Coordinates(-40., 'not a number')
