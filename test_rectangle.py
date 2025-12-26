import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_area_list(self):
        with self.assertRaises(TypeError):
            area([5])

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_perimeter_list(self):
        with self.assertRaises(TypeError):
            perimeter([3])

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()
