import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equal_sides(self):
        self.assertEqual(perimeter(5, 5, 5), 15)


if __name__ == '__main__':
    unittest.main()
