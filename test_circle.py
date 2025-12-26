import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-5), math.pi * 25)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_area_list(self):
        with self.assertRaises(TypeError):
            area([5])

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_area_boolean(self):
        self.assertEqual(area(True), math.pi * 1)
        self.assertEqual(area(False), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3), 2 * math.pi * -3)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_perimeter_list(self):
        with self.assertRaises(TypeError):
            perimeter([3])

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_perimeter_boolean(self):
        self.assertEqual(perimeter(True), 2 * math.pi * 1)
        self.assertEqual(perimeter(False), 0)


if __name__ == '__main__':
    unittest.main()
